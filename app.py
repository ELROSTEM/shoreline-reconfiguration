import streamlit as st

from apps import ai, data, storyboard
from multiapp import MultiApp

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Storyboard", storyboard.app)
apps.add_app("Ai", ai.app)
apps.add_app("Data", data.app)
# The main app
apps.run()
