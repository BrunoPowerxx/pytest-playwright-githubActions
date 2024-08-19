import streamlit as st
import pandas as pd
import streamlit_pandas as sp

file = "california_housing_test.csv"
df = pd.read_csv(file)

all_widgets = sp.create_widgets(df)
res = sp.filter_df(df, all_widgets)
st.title("Streamlit AutoPandas")
st.header("Original DataFrame")
st.write(df)

st.header("Result DataFrame")
st.write(res)
