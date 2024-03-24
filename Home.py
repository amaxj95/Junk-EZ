import streamlit as st
import webbrowser
from send_email import send_email

st.set_page_config(layout="wide")

# Centered header and subheader
st.markdown("<h1 style='text-align: center;'>Welcome to the Junk-EZ Co.'s Online Service Station</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>The easy Upcycling & Hauling System</h2>", unsafe_allow_html=True)

# Centered content
st.markdown("<p style='text-align: center;'>We specialize in Curbside trash Valet and Junk Removal. At Junk-EZ we make"
            "hauling junk and getting debris removed EZ. For now, our drivers take your items to a local landfill. As "
            "we"
            "grow we look forward revolutionizing our waste management system. We understand that no one wants to "
            "handle"
            "trash. So we’ve created a patent-pending system that allows for all users to make money by responsibly"
            "recycling. To get started, navigate to the Junk&Debris or Curbside collection pages to get started</p>", unsafe_allow_html=True)
