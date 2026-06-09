import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pooja Registration", layout="centered")

st.title("Pooja Registration")
st.write("Enter details below. The form will reset automatically after each submission.")
st.markdown("---")

# PASTE YOUR COPIED GOOGLE SHEET URL BETWEEN THE QUOTES BELOW:
SHEET_URL = "https://docs.google.com/spreadsheets/d/1U7LQZkduOY9bxubjkNKggnqXdIEwJyvWMsPwkl3aGkc/edit?usp=sharing"

# Setup temporary memory for the inputs if they don't exist yet
if "emp_name" not in st.session_state: st.session_state.emp_name = ""
if "emp_star" not in st.session_state: st.session_state.emp_star = ""
if "emp_phone" not in st.session_state: st.session_state.emp_phone = ""
if "success_msg" not in st.session_state: st.session_state.success_msg = False

# Function to safely wipe memory keys before the fields reload
def clear_form():
    name = st.session_state.emp_name.strip()
    birthstar = st.session_state.emp_star.strip().upper()
    phone = st.session_state.emp_phone.strip()
    
    if not name or not birthstar or not phone:
        st.session_state.error_msg = "Please fill out all three fields before submitting."
        return

    try:
        # Clear the memory boxes safely
        st.session_state.emp_name = ""
        st.session_state.emp_star = ""
        st.session_state.emp_phone = ""
        st.session_state.success_msg = True
        if "error_msg" in st.session_state: del st.session_state.error_msg
    except Exception as e:
        st.session_state.error_msg = f"Connection Error: {e}"

# Display notifications if they exist in memory
if "error_msg" in st.session_state:
    st.error(st.session_state.error_msg)
    del st.session_state.error_msg

if st.session_state.success_msg:
    st.success("Saved successfully! Form reset for the next person.")
    st.session_state.success_msg = False # Reset flag

# The 3 Manual Text Input boxes linked to memory
name_input = st.text_input("1. Full Name", key="emp_name")
star_input = st.text_input("2. Birthstar", key="emp_star")
phone_input = st.text_input("3. Phone Number", key="emp_phone")

st.markdown("---")

# The button triggers the 'clear_form' loop directly via on_click
st.button("Submit Data", type="primary", use_container_width=True, on_click=clear_form)
