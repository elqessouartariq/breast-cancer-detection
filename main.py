import streamlit as st
from Tabs import home, predict, visualise, about
from web_functions import load_data


# Configure the app
st.set_page_config(
    page_title = 'Breast Cancer Detection',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "About": about,
    "Prediction": predict,
    "Visualisation": visualise
}

st.sidebar.title("Navigation")

page = st.sidebar.radio("Pages", list(Tabs.keys()))

df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
