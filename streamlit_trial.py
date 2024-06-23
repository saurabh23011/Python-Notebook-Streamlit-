import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Python Notebook')

st.write("Write your Python code below and press 'Run' to execute.")

code = st.text_area("Code", height=300)

run_button = st.button("Run")

if run_button:
    try:
        
        exec(code)
    except Exception as e:
        st.error(f"Error executing code: {e}")



