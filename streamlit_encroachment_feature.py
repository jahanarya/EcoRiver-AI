
import streamlit as st
import pickle
from encroachment_utils import preprocess_image
from PIL import Image

# Load model
with open("encroachment_model.pkl", "rb") as f:
    model = pickle.load(f)

st.subheader("🧠 AI Encroachment Detection")
uploaded_file = st.file_uploader("Upload a satellite image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.info("Analyzing...")
    X = preprocess_image(image)
    prediction = model.predict(X)[0]
    confidence = max(model.predict_proba(X)[0]) * 100

    if prediction == 1:
        st.error(f"⚠️ Encroachment Detected (Confidence: {confidence:.1f}%)")
    else:
        st.success(f"✅ No Encroachment Detected (Confidence: {confidence:.1f}%)")
