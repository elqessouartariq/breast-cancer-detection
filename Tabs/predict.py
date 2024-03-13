import streamlit as st
from web_functions import predict

def app(df, X, y):

    st.title("Detect Breast Cancer")

    st.subheader("Select Values:")

    col1, col2, col3 = st.columns(3)

    with col1:
        # Take input of features from the user.
        rad = st.number_input("Radius", float(df["radius_mean"].min()), float(df["radius_mean"].max()))
        tex = st.number_input("Texture", float(df["texture_mean"].min()), float(df["texture_mean"].max()))
        per = st.number_input("Perimeter", float(df["perimeter_mean"].min()), float(df["perimeter_mean"].max()))

    with col2:
        are = st.number_input("Area", float(df["area_mean"].min()), float(df["area_mean"].max()))
        smo = st.number_input("Smoothness", float(df["smoothness_mean"].min()), float(df["smoothness_mean"].max()))
        com = st.number_input("Compactness", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    with col3:
        con = st.number_input("Concavity", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
        sym = st.number_input("Symmetry", float(df["symmetry_mean"].min()), float(df["symmetry_mean"].max()))
        fad = st.number_input("Fractal Dimension", float(df["fractal_dimension_mean"].min()), float(df["fractal_dimension_mean"].max()))

    # Create a list to store all the features
    features = [rad,tex,per,are,smo,com,con,sym,fad]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person has Breast Cancer!!")
        else:
            st.success("The person is safe from Breast Cancer")
