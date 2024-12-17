document.getElementById('uploadButton').addEventListener('click', () => {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', async function() {
    const file = this.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    // Show the "Processing..." message
    document.getElementById('loading').style.display = 'block';
    document.getElementById('output').innerHTML = ''; // Clear previous results

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();

    // Hide the "Processing..." message
    document.getElementById('loading').style.display = 'none';

    if (response.ok) {
        document.getElementById('output').innerHTML = `
            <h3>Identified Medicine: ${result.medicine}</h3>
            <p>Confidence Score: ${result.score}</p>
        `;
    } else {
        document.getElementById('output').innerHTML = `
            <h3>Error: ${result.error}</h3>
        `;
    }
});
