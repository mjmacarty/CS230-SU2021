import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
st.write("# Hello")

x = 1000
x

"""
# Docstrings get rendered as markdown
* markdown is simplfied HTML
* to get some examples: [visit stackedit.io](https://stackedit.io)
"""
st.sidebar.header("Sidebar")
st.sidebar.selectbox(label = "Choose one...", options = ["Eeeny", "Meeny", "Miny", "Mo"])

y = np.random.standard_normal(10000)
st.line_chart(y)
scale_hist = np.array(range(0,1500, 250))
fig, (axes1,axes2) = plt.subplots(2,1, figsize=(2,2))
axes1.set_yticks(scale_hist)
axes1.set_yticklabels(scale_hist, fontsize=3)
axes1.set_xticks(list(range(-3,4,1)))
axes1.set_xticklabels(list(range(-3,4,1)), fontsize=3)
axes1.hist(y, bins = 25, edgecolor = 'w')
axes2.plot(y.cumsum())
y_max = math.ceil(max(y.cumsum())/ 10) * 10
y_min = min(y.cumsum())// 10 * 10
axes2.set_yticks(np.linspace(y_min,y_max,11))
axes2.set_yticklabels(np.linspace(y_min,y_max,11), fontsize= 3)
axes2.set_xticklabels("", fontsize = 3)
y_max
y_min
st.pyplot(fig)

st.line_chart(y.cumsum())