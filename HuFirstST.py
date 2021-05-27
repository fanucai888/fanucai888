import streamlit as st
import numpy as np
import pandas as pd

st.title("Hu's first ST program")

st.write('Hello FANUC')
st.title("Hello Oshino Village")
st.write("# Welcome to Oshino village")
st.write("## Oshino village is located in Japan")
st.write("### A CNC and robot company named FANUC is located here")

# df = pd.DataFrame({
#     'name':["Wang","Hu","Ma","Xia"],
#     'age':[60,34,30,65]
# })

# st.dataframe(df.highlight,width=200,height=100)

# FANUC locats at [35.44553, 138.83849]
df = pd.DataFrame(
    np.random.randn(10,2) / [100,100] + np.array([35.44553, 138.83849]),
    columns=["lat","lon"]
)

st.map(df)