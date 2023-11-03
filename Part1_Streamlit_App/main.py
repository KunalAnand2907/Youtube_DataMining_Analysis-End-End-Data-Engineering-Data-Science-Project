import streamlit as st

# for creating Navigation Pane
from streamlit_option_menu import option_menu

# Importing the 5 files in this main File
import about,account,home,trending,Your_posts

st.set_page_config(layout='wide',page_title = 'YouTube Data Mining & Analysis - End-End Data Engineering & Data Science Project',page_icon=':iphone:')

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self,title,function):
        self.apps.append({"title":title,"function":function})

    def run():
        st.sidebar.subheader("YouTube Data Mining & Analysis: :blue[End - End Data Engineering & Data Science Project]", divider='rainbow')
        with st.sidebar:  # the Navigation Pane that we are creating
            app = option_menu(
                menu_title= None,
                options = ['Home','Account','Youtube Channels Data Analysis via Web Scrapping','Your Posts, Notes & Queries','About'],
                icons = ['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon = 'chat-test-fill',
                default_index= 1,
                styles= {
                    "container": {"padding": "3!important","background-color":'black',"font-size": "7px"},
        "icon": {"color": "white", "font-size": "19px"},
        "nav-link": {"color":"white","font-size": "13px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                )

        if app == "Home": # call the file.func if it is the mentioned option
            home.app()
        if app == "Account":
            account.app()
        if app == "Youtube Channels Data Analysis via Web Scrapping":
            trending.app()
        if app == 'Your Posts, Notes & Queries':
            Your_posts.app()
        if app == 'About':
            about.app()


    run()