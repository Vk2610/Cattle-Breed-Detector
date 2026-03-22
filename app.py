import streamlit as st
import torch
import torch.nn.functional as F
from PIL import Image
import json
import time

from model.model import CattleModel
from utils.preprocess import transform

# -------------------------------------------------------------
# 1. Page Configuration
# -------------------------------------------------------------
st.set_page_config(
    page_title="Cattle Breed AI",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# 2. Custom CSS Styling (Theme Aware)
# -------------------------------------------------------------
st.markdown("""
<style>
    .prediction-card {
        background-color: var(--secondary-background-color);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 24px;
        transition: transform 0.3s ease;
    }
    .prediction-card:hover {
        transform: translateY(-5px);
    }
    .top-prediction-label {
        font-size: 1.1rem;
        margin-bottom: 8px;
        opacity: 0.8;
        font-weight: 500;
    }
    .top-breed-name {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .top-confidence {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2ecc71;
    }
    .main-header {
        text-align: center;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. Model Loading & Caching
# -------------------------------------------------------------
@st.cache_resource(show_spinner="Loading AI Core Models into Memory...")
def load_app_data():
    with open("utils/labels.json") as f:
        labels = json.load(f)
    model = CattleModel(num_classes=len(labels))
    model.load_state_dict(torch.load("model/model.pth", map_location=torch.device('cpu')))
    model.eval()
    return labels, model

labels, model = load_app_data()

# -------------------------------------------------------------
# 4. App Interface
# -------------------------------------------------------------
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🐄 Intelligent Cattle Breed Classifier")
st.markdown("#### Upload a photo of a cattle to instantly identify its breed using Deep Learning.")
st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# Upload Section Layout
col_upload, col_empty = st.columns([1, 1])
with col_upload:
    uploaded_file = st.file_uploader("Select or Drag & Drop an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Elegant 2-column layout for Image vs Results
    col1, col_spacer, col2 = st.columns([1.2, 0.1, 1])

    with col1:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Original Upload")

    with col2:
        st.subheader("⚙️ AI Analysis Results")
        
        # Spinner for aesthetic purpose
        with st.spinner("Analyzing anatomical features..."):
            time.sleep(0.6) # Artifical micro-delay for UX finish
            
            img_tensor = transform(image).unsqueeze(0)
            
            with torch.no_grad():
                output = model(img_tensor)
                # Apply softmax to get normalized probabilities (0.0 to 1.0)
                probabilities = F.softmax(output[0], dim=0)
                
                # Extract Top 5 probabilities and class indices
                top_probs, top_indices = torch.topk(probabilities, 5)
            
            primary_breed = labels[top_indices[0].item()].title().replace("_", " ")
            primary_conf = top_probs[0].item() * 100
            
            # Reject predictions with suspiciously low confidence (likely not a cattle)
            if primary_conf < 65.0:
                st.error("⚠️ **Unrecognized Image**")
                st.write("The AI is not confident this image contains a recognized cattle breed. Please ensure you are uploading a clear photograph of a cattle.")
                st.info(f"*(Highest detected match was {primary_breed} at only {primary_conf:.1f}% confidence)*")
            else:
                # Display primary prediction highlight card
                st.markdown(f"""
                <div class="prediction-card">
                    <div class="top-prediction-label">Top Prediction</div>
                    <div class="top-breed-name">{primary_breed}</div>
                    <div class="top-confidence">{primary_conf:.1f}% Confidence</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.divider()
                st.markdown("#### Confidence Breakdown (Top 5)")
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Display granular breakdown
                for i in range(5):
                    idx = top_indices[i].item()
                    prob = top_probs[i].item()
                    breed_name = labels[idx].title().replace("_", " ")
                    
                    pct = prob * 100
                    st.markdown(f"**{i+1}. {breed_name}** &mdash; `{pct:.1f}%`")
                    st.progress(prob)