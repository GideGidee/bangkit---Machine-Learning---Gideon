import streamlit as st 
import datetime
import pandas as pd

st.header("Text input:")
name = st.text_input(label="Nama lengkap", value="")
st.write("Nama: ", name)

st.header("Text-area:")
text = st.text_area("Feedback")
st.write("Feedback: ", text)

st.header("Number input:")
number = st.number_input(label="Umur")
st.write("Umur: ", str(number), " tahun")

st.header("Date input: ")
date = st.date_input(label="Tanggal lahir", min_value=datetime.date(1900, 1, 1))
st.write("Tanggal lahir:", date)

st.header("File uploader: ")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    except:
        st.write("Please upload csv file!")

st.header("Camera input: ")
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

st.header("Button: ")
if st.button("Say hello"):
    st.write("Hello there")

st.header("Checkbox: ")
agree = st.checkbox("I agree")
if agree:
    st.write("Welcome to MyApp")

st.header("Radio button: ")
genre = st.radio(
    label="What's your favorite movie genre",
    options=("Comedy", "Drama", "Documentary"),
    horizontal=False,
)

st.header("Select box: ")
genre = st.selectbox(
    label="What's your favorite movie genre", options=("Comedy", "Drama", "Documentary")
)

st.header("Multiselect: ")
genre = st.multiselect(
    label="What's your favorite movie genre", options=("Comedy", "Drama", "Documentary")
)

st.header("Slider:")
values = st.slider(
    label="Select a range of values", min_value=0, max_value=100, value=(0, 100)
)
st.write("Values:", values)