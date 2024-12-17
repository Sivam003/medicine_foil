# **Medicine Foil Name Detection Using AI 📷💊**

This project is an AI-based system that identifies the name of medicines from torn foil images using **OpenCV**, **EasyOCR**, and **Flask**. It combines **Computer Vision**, **Optical Character Recognition (OCR)**, and **Machine Learning** for accurate and efficient medicine name prediction.

---

## **Project Workflow 🛠️**

1. **Image Upload**:  
   The user uploads a torn medicine foil image via the web interface.  

2. **Preprocessing with OpenCV**:  
   - Converts the image to grayscale.  
   - Reduces noise for better text detection.  
   - Enhances image features for OCR.  

3. **Text Extraction with EasyOCR**:  
   - OCR extracts readable text from the foil image.  

4. **Text Matching**:  
   - Extracted text is compared with a predefined database using **Pandas** and **FuzzyWuzzy** for similarity scoring.  

5. **Prediction Display**:  
   - The predicted medicine name is displayed to the user.  
   - A "Processing..." buffer animation is shown during image analysis.  

---

## **Technologies Used 🚀**

### **Software**  
- **Front-end**:  
  - **HTML**: For structuring the web interface.  
  - **CSS**: For styling and responsive design.  
  - **JavaScript**: To add interactivity and display buffer animations.  
- **Back-end**:  
  - **Flask**: Lightweight Python web framework to handle requests and responses.  
  - **Python Libraries**:  
    - **OpenCV**: For image preprocessing and enhancement.  
    - **EasyOCR**: For text extraction from images.  
    - **Pandas**: To handle and manipulate the medicine dataset.  
    - **FuzzyWuzzy**: For fuzzy matching of extracted text with the dataset.  

### **Hardware**  
- **RAM**: Minimum 4 GB  
- **Hard Disk**: Minimum 1 GB of free space  
- **Operating System**: Windows 10 / Ubuntu 20.04  
- **Editor**: Visual Studio Code / PyCharm  
- **Browser**: Google Chrome  

---

## **Project Setup and Installation ⚙️**

Follow these steps to set up and run the project locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/foil-finder.git
   cd foil-finder
2. **Install required libraries**
   ```bash
   pip install flask opencv-python easyocr pandas fuzzywuzzy python-Levenshtein
3. **Add the Dataset**
   Place the Medicine_Details.csv file in the root directory. This file contains the medicine names and compositions.
4. **Run the Project**
   ```bash
   python app.py
5, **Access the website**
   Open a browser and visit http://127.0.0.1:5000/.
