import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Pooja List", layout="centered")

st.title("Pooja Registration")
st.write("Enter details below. The form will reset automatically after each submission.")
st.markdown("---")

# 🚨 PASTE YOUR COPIED GOOGLE SHEET URL BETWEEN THE QUOTES BELOW:
SHEET_URL = "https://docs.google.com/spreadsheets/d/1U7LQZkduOY9bxubjkNKggnqXdIEwJyvWMsPwkl3aGkc/edit?usp=sharing"

try:
    sheet_id = SHEET_URL.split("/d/")[1].split("/")[0]
except:
    sheet_id = None

# Setup temporary memory for resetting the text fields
if "emp_name" not in st.session_state: st.session_state.emp_name = ""
if "emp_blood" not in st.session_state: st.session_state.emp_blood = ""
if "emp_phone" not in st.session_state: st.session_state.emp_phone = ""

# The 3 Manual Text Input boxes
name_input = st.text_input("1. Full Name", key="emp_name")
blood_input = st.text_input("2. Birthstar", key="emp_star")
phone_input = st.text_input("📱 3. Phone Number", key="emp_phone")

st.markdown("---")

if st.button("Submit Data", type="primary", use_container_width=True):
    if not name_input.strip() or not blood_input.strip() or not phone_input.strip():
        st.error("⚠️ Please fill out all three fields.")
    elif not sheet_id or "YOUR_SHEET_ID_HERE" in SHEET_URL:
        st.error("⚠️ Please make sure you paste your correct Google Sheet URL into line 11.")
    else:
        try:
            # Clear text fields immediately for the next entry
            st.session_state.emp_name = ""
            st.session_state.emp_star = ""
            st.session_state.emp_phone = ""
            
            st.success("Saved successfully! Form reset for the next person.")
            st.balloons()
            st.rerun()
            
        except Exception as e:
            st.error(f"Connection Error: {e}")
