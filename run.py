import streamlit as st
import pandas as pd
import os

st.title("Excel File Uploader with Save")

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Create temp folder to save uploaded file
    os.makedirs("temp", exist_ok=True)

    # Save uploaded file to disk
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Read the Excel file using pandas
    try:
        df = pd.read_excel(file_path)
        st.success("File uploaded and read successfully!")
        st.subheader("Preview of Uploaded Excel")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
