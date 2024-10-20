import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
figure = plt.figure()

st.markdown("<h1 style = 'text-align: center;'>Data Vistualizer </h1>",unsafe_allow_html=True)

files_names = list()
files = st.file_uploader("Upload Multiple Files",type=["xlsx","parquet"],accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
    #print(files_names)
    selected_files = st.multiselect("Select Files", options=files_names)
    if selected_files:
        option = st.radio("Select Entity Against Date:",options=["None","REVENUE","UNIT"])
        if option != "None":
            for file in files:
                df = pd.read_excel(file)
                #print(df.head())
                plt.plot(df['DATE'], df[option], label=file.name, marker='o')  # Line plot with markers
                plt.title(option+ " Chart")  # Title of the plot
                plt.xlabel("DATE")  # X-axis label
                plt.ylabel(option)  # Y-axis label
                plt.grid(True)  # Show grid
                plt.xticks(df['DATE'])  # Set x-ticks to match years
                plt.gcf().autofmt_xdate()
                plt.legend()
            st.write(figure)
            ###
            