import streamlit as st
import pandas as pd
import numpy as np

#sets the page to wide layout which is not automatic
st.set_page_config(layout = 'wide')
st.title("My Streamlit App")
st.header("Metrics", divider="green")


# Create a simple DataFrame
data = {
    'Column1': np.random.randint(1, 200, 30)
}

df = pd.DataFrame(data)

col1, col2, col3 = st.columns(3)
col1.metric("Temp", 42.7, f"{-2}%")
col2.metric("Rain", 71, f"{11}%")
col3.metric("Gas price", 3.5, f"{-1}")

st.subheader("Line Charts", divider="red")
st.line_chart(df["Column1"])