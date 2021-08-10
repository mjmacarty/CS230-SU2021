import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
st.write("# Hello")
st.header("Here's a built-in header")
st.write("Basic text from write")
x = 1000
st.write(f"# {x}")

"""
# Docstring
* rendered as markdown
* markdown is simplfied HTML
* [examples of markdown](https://stackedit.io)
* *italics*
* **bold**
"""

arr = np.arange(10).reshape(2,5)
arr

st.sidebar.header("Our Sideber")
st.sidebar.selectbox(label = "Choices", options = ['Eeny', 'Meeny', 'Miny', 'Mo'])