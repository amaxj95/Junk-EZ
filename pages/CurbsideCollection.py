import webbrowser
import streamlit as st
from send_email import send_email

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_1490.png")  # add logo.png

with col2:
    st.header("Schedule your pickup!")
    content = """Our 96 Gallon trash bins are designed to be used as curbside trash bins that you would typically drag 
    to the end of the curb on a given day of the week. We differ from our competitors by allowing our customers (you),
    to schedule your pickup whenever your bin is full, Up to 4 times a month. Please note, that a curbside pickup is 
    different from a junk haul. If you have junk removal items to send in, then you will be billed accordingly, and we 
    will not count the pickup to your curbside count. One week of free curbside pickup whenever you book a junk haul. 
    For one time pickups, just place your bags on the curb and we'll be by immediately to pick them up.    
"""
    st.write(content)

    with st.form(key="email_forms"):
        user_email = st.text_input("Enter Your Email")
        user_address = st.text_input("Enter Your Address")
        user_phone = st.text_input("Enter phone number")
        freq_option = st.selectbox('Pickup Frequency', ('One Time', 'Monthly', 'Quarterly'))
        first_time_customer = st.selectbox('First Scheduled Pickup?', ('Yes', 'No'))
        raw_message = st.text_area("Enter any pickup notes here...")

        # Define the Stripe checkout links based on pickup frequency
        checkout_links = {
            'One Time': 'https://buy.stripe.com/5kA5ocbAs9r2dbi14j',
            'Monthly': 'https://buy.stripe.com/8wM4k88og46Ic7e6ou',
            'Quarterly': 'https://buy.stripe.com/5kAeYMbAs32E3AI4gt'
        }

        # Define the alert message for quarterly package offer
        quarterly_offer_alert = ("Sign up for our quarterly package today and get the first 3 months free when you "
                                 "purchase a trash bin! "
                                 "[Click here to learn more](https://buy.stripe.com/dR67wk7kcfPq3AI008)")

        message = f"""\
Subject: New Curbside Service Request from {user_email}

    From: {user_email}
    Address: {user_address}
    Phone: {user_phone}
    Frequency: {freq_option}
    First Time: {first_time_customer}
    Notes: {raw_message}"""

        # Boolean variable to track whether the form can be submitted
        can_submit = False

        # Check if all fields are filled
        if user_email and user_address and user_phone and freq_option and first_time_customer:
            can_submit = True

        # Display warning message if any field is empty
        if not can_submit:
            st.warning("Please fill in all required fields.")

        # Display submit button and proceed to checkout if all fields are filled
        if st.form_submit_button("Proceed to Checkout") and can_submit:
            checkout_url = checkout_links[freq_option]
            webbrowser.open_new_tab(checkout_url)
            send_email(message)
            st.info("Pickup Scheduled, We'll see you soon!")
