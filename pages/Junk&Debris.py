import streamlit as st
import webbrowser
from send_email import send_email

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_1490.png")  # add logo.png

with col2:
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("Junk & Debris Removal!")
    content = """Our primary service is Junk & Debris Removal. We do flat rate hauls which removes hidden fees & 
    inconveniences. Our Junk & Debris removal service is perfect for home cleanups, yard waste removal*, seasonal 
    decluttering & move-outs. Some items like mattresses, tires, propane tanks, paint cans, and Hazmat containers will 
    incur a one-time 50 special care fee as our recyclers do not typically take those items. We have 3 pricing tiers
    for a full truck load is 350. A half truck is 275, and a quarter truck is 225. We also offer light demolition for 
    items like patios & decks, above-ground pools, hot tubs, and sheds. Light Demolition starts at 450."""
    st.write(content)

    with st.form(key="email_forms"):
        user_email = st.text_input("Enter Your Email")
        user_address = st.text_input("Enter Your Address")
        user_phone = st.text_input("Enter phone number")
        pickup_option = st.selectbox('Pickup Type', ('Quarter-Truck', 'Half-Truck', 'Full-Truck'))
        pickup_time = st.time_input('What time would you like for us to arrive?', value=None)
        pickup_date = st.date_input('What date would you like')
        raw_message = st.text_area("Enter any pickup notes here...")

        # Define the Stripe checkout links for each pickup option
        checkout_links = {
            'Quarter-Truck': 'https://buy.stripe.com/aEUeYM9sk8mYgnudR0',
            'Half-Truck': 'https://buy.stripe.com/3cs9EsfQIeLm8V2eV3',
            'Full-Truck': 'https://buy.stripe.com/3csg2Q4805aMb3a3cf'
        }

        message = f"""\
        Subject: New Junk Removal Request from {user_email}

            From: {user_email}
            Address: {user_address}
            Phone: {user_phone}
            Frequency: {pickup_option}
            Pickup Time: {pickup_time}
            Pickup Date: {pickup_date}
            Notes: {raw_message}"""

        # Boolean variable to track whether the form can be submitted
        can_submit = False

        # Check if all fields are filled
        if user_email and user_address and user_phone and pickup_option and pickup_time and pickup_date:
            can_submit = True

        # Display warning message if any field is empty
        if not can_submit:
            st.warning("Please fill in all required fields.")

        # Display submit button and proceed to checkout if all fields are filled
        if st.form_submit_button("Proceed to Checkout") and can_submit:
            checkout_url = checkout_links[pickup_option]
            webbrowser.open_new_tab(checkout_url)
            send_email(message)
            st.info("Pickup Scheduled, We'll see you soon!")
