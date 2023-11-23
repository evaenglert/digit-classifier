import streamlit as st
from fastbook import *

st.markdown("""# This is a header""")
line_count = st.slider("Select a line count", 1, 10, 3)

path = Path()
learner = load_learner(path/"digit_classifier_tiny.pkl")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    prediction = learner.predict(tensor(image))
    st.markdown(prediction)
