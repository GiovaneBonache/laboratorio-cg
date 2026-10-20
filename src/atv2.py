import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

imagem = np.zeros((8, 8), dtype=np.uint8)

imagem[2, 5] = 255

imagem[4:, :] = 128

st.image(ampliar(imagem))
st.write(imagem)

bandeira = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira[:2] = (110, 50, 150)
bandeira[2:4] = (240, 190, 40)
bandeira[4:] = (30, 160, 150)
st.image(ampliar(bandeira))

bandeira2 = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira2[0] = (228, 3, 3)
bandeira2[1] = (255, 140, 0)
bandeira2[2] = (255, 237, 0)
bandeira2[3] = (0, 128, 38)
bandeira2[4] = (0, 77, 255)
bandeira2[5] = (117, 7, 135)
st.image(ampliar(bandeira2))


bandeira3 = np.zeros((36, 54, 3), dtype=np.uint8)

for i in range(36):
    for j in range(54):
        t = j - (36 - i) * 1.5 

        if t < -8:
            bandeira3[i, j] = (59, 90, 163) 
        elif t < -5:
            bandeira3[i, j] = (255, 255, 255) 
        elif t <= 5:
            bandeira3[i, j] = (190, 0, 39)   
        elif t <= 8:
            bandeira3[i, j] = (255, 255, 255) 
        else:
            bandeira3[i, j] = (35, 159, 76)   

for i in range(36):
    for j in range(54):
        d2 = (i - 9)**2 + (j - 11)**2
        if d2 <= 36:
            bandeira3[i, j] = (250, 240, 0)
        if d2 <= 12:
            bandeira3[i, j] = (59, 90, 163)

st.image(ampliar(bandeira3))
