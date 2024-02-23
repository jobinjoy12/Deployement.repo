import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('KKK aanu nee')
<img src="https://2.bp.blogspot.com/-ejF-Plyv4_s/UcE2uceM4zI/AAAAAAAAANw/vx_iKjbZRb0/s1600/vlcsnap-2013-06-18-19h22m27s107.png" />
st.markdown('Toy model to play to classify iris flowers into \
     (setosa, versicolor, virginica) based on their sepal/petal \
    and length/width.')

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)

with col2:
    st.text("Pepal characteristics")
    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)

st.text('')
if st.button("Predict type of Iris"):
    result = predict(
        np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    st.text(result[0])


st.text('')
st.text('')
st.markdown(
    '`Create by` [Jobinjoy-Ponnappal](https://github.com/jobinjoy12) | \
         `Code:` [GitHub](https://github.com/intel-unnati-saintgits/Model-Deployment-Demo/edit/main/app.py)')
