import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Imagem como matriz")

v = np.array([10, 20, 30])

m = np.array([[10, 20, 30],
              [40, 50, 60]])

c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

s = np.zeros((2, 3))
print(s.shape) 
print(s.dtype)