import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Pooja Registration", layout="centered")

st.title("Pooja Registration")
st.write("Enter details below. The form will reset automatically after each submission.")
st.markdown("---")

# Establish direct connection with Google Sheets via Streamlit Secrets
conn = st.connection("gsheets", type=GSheetsConnection)

# Setup temporary memory for inputs
if "emp_name" not in st.session_state: st.session_state.emp_name = ""
if "emp_star" not in st.session_state: st.session_state.emp_star = ""
if "emp_phone" not in st.session_state: st.session_state.emp_phone = ""
if "success_msg" not in st.session_state: st.session_state.success_msg = False

# Function to write data and safely wipe fields before reloading
def clear_form():
    name = st.session_state.emp_name.strip()
    birthstar = st.session_state.emp_star.strip().upper()
    phone = st.session_state.emp_phone.strip()
    
    if not name or not birthstar or not phone:
        st.session_state.error_msg = "Please fill out all three fields before submitting."
        return

    try:
        # Read the current layout and rows of your Google Sheet (ttl=0 clears cached versions)
        existing_data = conn.read(worksheet="Sheet1", ttl=0)
        
        # Package the new entry into a data row
        new_row = pd.DataFrame([{
            "Name": name,
            "Birthstar": birthstar,
            "Phone Number": phone
        }])
        
        # Merge new row to old data and push it right back to the spreadsheet link
        updated_data = pd.concat([existing_data, new_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_data)
        
        # Clear the text input frames for the next entry
        st.session_state.emp_name = ""
        st.session_state.emp_star = ""
        st.session_state.emp_phone = ""
        st.session_state.success_msg = True
        if "error_msg" in st.session_state: del st.session_state.error_msg
    except Exception as e:
        st.session_state.error_msg = f"Connection Error: {e}"

# Display matching warning alerts or success prompts on screen
if "error_msg" in st.session_state:
    st.error(st.session_state.error_msg)
    del st.session_state.error_msg

if st.session_state.success_msg:
    st.success("Saved successfully! Form reset for the next person.")
    st.session_state.success_msg = False 

# The 3 Input Fields linked directly to memory frames
name_input = st.text_input("1. Full Name", key="emp_name")
star_input = st.text_input("2. Birthstar", key="emp_star")
phone_input = st.text_input("3. Phone Number", key="emp_phone")

st.markdown("---")

# Submit button triggers data execution loop on_click
st.button("Submit Data", type="primary", use_container_width=True, on_click=clear_form)
