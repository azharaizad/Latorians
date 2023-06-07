import streamlit as st
from home import HomePage
from CancerCervixUI import CancerCervixPage

class SessionState:
    def __init__(self) :
        self.page = "Home"

state = SessionState()

pages = {
    "Home Page": HomePage(),
    "Predict Cancer Cervix": CancerCervixPage()
}

def render_page():
    if state.page in pages:
        pages[state.page].render()

def main():
    st.sidebar.title("Hi There !!!")
    selected_page = st.sidebar.radio("Go to", tuple(pages.keys()))
    state.page = selected_page

    render_page()

if __name__=="__main__":
    main()