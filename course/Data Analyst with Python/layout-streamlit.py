import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# sidebar
st.title("Belajar analisis data")

with st.sidebar:
    st.text("ini sidebar")

    values = st.slider(
        label = "select a range of values",
        min_value = 0, max_value = 100, value = (0, 100)
    )
    st.write("Values:", values)

# tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    # columns
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.header("Kolom 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("Kolom 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("Kolom 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")

with tab2:
    # container
    with st.container():
        st.header("Inside the container")

        x = np.random.normal(15, 5, 250)
        fig, ax = plt.subplots()
        ax.hist(x=x, bins=15)
        st.pyplot(fig) 
    st.write("Outside the container")

with tab3:
    # expander
    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

    with st.expander("See explanation"):
        st.write(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
            in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            """
        )