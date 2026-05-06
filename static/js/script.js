const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const previewImg = document.getElementById('previewImg');
const loading = document.getElementById('loading');
const resultCard = document.getElementById('resultCard');
const uploadBox = document.getElementById('uploadBox');



fileInput.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Hide upload box and show preview
    uploadBox.style.display = 'none';
    previewImg.src = URL.createObjectURL(file);
    previewSection.style.display = 'block';

    // Show loading
    loading.style.display = 'block';
    resultCard.style.display = 'none';
    document.getElementById('warningCard').style.display = 'none';

    try {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        loading.style.display = 'none';

        if (data.error) {
            showWarning();
            document.querySelector('#warningCard p').textContent = data.message;
        } else {
            // Show cattle prediction result
            resultCard.style.display = 'block';

            // Update result
            document.getElementById('breedName').textContent = data.prediction;
            document.getElementById('confidence').textContent = `${data.confidence}% Confidence`;
            document.getElementById('progressFill').style.width = `${data.confidence}%`;
        }
    } catch (error) {
        console.error('Error:', error);
        loading.style.display = 'none';
        alert('An error occurred during prediction.');
    }
});

// Add drag and drop functionality
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#38bdf8';
    uploadBox.style.background = 'rgba(56, 189, 248, 0.05)';
});

uploadBox.addEventListener('dragleave', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'rgba(255, 255, 255, 0.3)';
    uploadBox.style.background = 'transparent';
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'rgba(255, 255, 255, 0.3)';
    uploadBox.style.background = 'transparent';

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        // Create a new event to trigger the file input change
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(files[0]);
        fileInput.files = dataTransfer.files;

        // Trigger the change event
        const event = new Event('change', { bubbles: true });
        fileInput.dispatchEvent(event);
    }
});

// Show warning for non-cattle images
function showWarning() {
    document.getElementById('warningCard').style.display = 'block';
}

// Reset upload form
function resetUpload() {
    uploadBox.style.display = 'block';
    previewSection.style.display = 'none';
    resultCard.style.display = 'none';
    document.getElementById('warningCard').style.display = 'none';
    fileInput.value = '';
    document.getElementById('progressFill').style.width = '0%';
}

// Click on preview to reset
previewImg.addEventListener('click', resetUpload);