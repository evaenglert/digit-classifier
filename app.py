import streamlit as st

st.markdown("""# This is a header""")
line_count = st.slider("Select a line count", 1, 10, 3)
