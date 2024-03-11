import streamlit as st
from streamlit_option_menu import option_menu
from Tabs import home, predict, visualise, about
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Breast Cancer Detection',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

selected = option_menu(
    menu_title = None,
    options = ['Home','About', 'Prediction', 'Visualisation'],
    icons=['bi-house','bi-info-circle','bi-calculator','bi-diagram-3'],
    menu_icon='🔗',
    default_index=0,
    orientation='horizontal',
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "About": about,
    "Prediction": predict,
    "Visualisation": visualise
}

page = selected

df, X, y = load_data()

# Call the app function of the selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()