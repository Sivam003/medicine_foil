from flask import Flask, request, jsonify, render_template
import cv2
import easyocr
import pandas as pd
from fuzzywuzzy import process
import numpy as np

app = Flask(__name__)

# Load the dataset
dataset_path = "Medicine_Details.csv"
df = pd.read_csv(dataset_path)

# Home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Function to find the best match from the dataset using FuzzyWuzzy
def find_best_match(text, choices):
    best_match, score, _ = process.extractOne(text, choices)
    return best_match, score

# Function to calculate combined similarity score
def calculate_combined_similarity(med_name_text, salt_name_text):
    combined_scores = []

    for index, row in df.iterrows():
        med_name_similarity = process.extractOne(med_name_text, [row['Medicine Name']])[1]
        salt_name_similarity = process.extractOne(salt_name_text, [row['Composition']])[1]
        combined_score = (med_name_similarity + salt_name_similarity) / 2
        combined_scores.append((row['Medicine Name'], combined_score))

    best_combined_match = max(combined_scores, key=lambda x: x[1])
    return best_combined_match

# Route to process the image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']

    # Read the image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Instance text detector
    reader = easyocr.Reader(['en'], gpu=False)
    text_ = reader.readtext(img)

    detected_texts = []

    def estimate_font_size(bbox):
        height = abs(bbox[0][1] - bbox[2][1])
        return height

    for t_, t in enumerate(text_):
        bbox, text, score = t
        if score > 0.45:
            font_size = estimate_font_size(bbox)
            detected_texts.append((text, font_size, bbox))

    detected_texts.sort(key=lambda x: x[1], reverse=True)
    unique_font_sizes = sorted(set([t[1] for t in detected_texts]), reverse=True)
    margin = 0

    def group_font_sizes(font_sizes, margin):
        grouped_sizes = []
        while font_sizes:
            base_size = font_sizes.pop(0)
            group = [base_size]
            remaining = []
            for size in font_sizes:
                if abs(size - base_size) <= margin:
                    group.append(size)
                else:
                    remaining.append(size)
            grouped_sizes.append(group)
            font_sizes = remaining
        return grouped_sizes

    grouped_font_sizes = group_font_sizes(unique_font_sizes, margin)
    largest_font_group = grouped_font_sizes[0] if grouped_font_sizes else []
    second_largest_font_group = grouped_font_sizes[1] if len(grouped_font_sizes) > 1 else []

    classified_texts = []
    for text, font_size, bbox in detected_texts:
        classification = 'Unclassified'
        if font_size in largest_font_group:
            classification = 'Salt Name'
        elif font_size in second_largest_font_group:
            classification = 'Medicine Name'
        classified_texts.append((text, classification))

    med_name_text, salt_name_text = "", ""
    for text, classification in classified_texts:
        if classification == 'Medicine Name':
            med_name_text = text
        elif classification == 'Salt Name':
            salt_name_text = text

    if med_name_text and salt_name_text:
        best_match, combined_score = calculate_combined_similarity(med_name_text, salt_name_text)
        return jsonify({
            'medicine': best_match,
            'score': combined_score
        })

    return jsonify({'error': 'Could not classify text'}), 400

if __name__ == '__main__':
    app.run(debug=True)
