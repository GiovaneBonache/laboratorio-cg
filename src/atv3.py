import numpy as np
import streamlit as st

st.title("Giovane Abrantes Bonache")

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Padrão")

k = st.slider("k", 1, 20, 4)
y, x = np.indices((64, 64))

def padrao(x, y, k):
    return (((x-32)**2 + (y-32)**2) * k // 4) % 256

imagem = padrao(x, y, k).astype(np.uint8)
st.image(ampliar(imagem, 4))    

def teste(x, y, k):
    return ((((x/2)-1)**2 + (y**2)/(x+1)) * k // 4) % 256

imagem = teste(x, y, k).astype(np.uint8)
st.image(ampliar(imagem, 4))    