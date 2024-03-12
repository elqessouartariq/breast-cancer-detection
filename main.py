import streamlit as st
from streamlit_option_menu import option_menu
from Tabs import home, predict, visualise
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Breast Cancer Detection',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

selected = option_menu(
    menu_title = None,
    options = ['Home','Prediction', 'Visualisation'],
    icons=['bi-house','bi-calculator','bi-diagram-3'],
    menu_icon='🔗',
    default_index=0,
    orientation='horizontal',
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
}

page = selected

df, X, y = load_data()

# Call the app function of the selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()