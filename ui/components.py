
import streamlit as st

def card(title):
    with st.container():
        st.markdown(f"<div class='card'><h3>{title}</h3>", unsafe_allow_html=True)
        yield
        st.markdown("</div>", unsafe_allow_html=True)

def gradient_button(label):
    return st.button(label, key=label)
