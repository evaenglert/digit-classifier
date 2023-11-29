import streamlit as st
from fastbook import *
from streamlit_drawable_canvas import st_canvas


st.markdown("""# This is a header""")

path = Path()
learner = load_learner(path/"digit_classifier_tiny.pkl")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    prediction = learner.predict(tensor(image))
    st.markdown(prediction)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=3,
    stroke_color='#eee',
    background_color='#000000',
    update_streamlit=True,
    height=200,
    width=200,
    drawing_mode="freedraw",
    display_toolbar=True,
    key="full_app",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    st.markdown(canvas_result.image_data)
    rgba_image = Image.fromarray(canvas_result.image_data)
    rgb_image = rgba_image.convert('RGB')
    prediction = learner.predict(tensor(rgb_image))
    st.markdown(prediction)
if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"])
    for col in objects.select_dtypes(include=["object"]).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)
