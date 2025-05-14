# importe das bibliotecas
import streamlit as st # interface bonitinha
import numpy as np # arrays e matematica 
import cv2 # processar openCV
from PIL import Image # manipulação de imagem com a Pillow
from filtros import aplicar_filtro
from transformacoes import aplicar_transformacao
from utils import salvar_para_download

#titulo
st.title("Visualizador de Imagens com Streamlit")

#upload
uploaded_file = st.file_uploader("Carregue uma imagem", type=["jpg", "jpeg", "png", "bmp"])

#condição da imagem carregada ou não
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

#exibe a img original na interface
    st.image(image, caption="Imagem Original", use_column_width=True)

#seletor de filtro e transformação
    filtro = st.selectbox("Escolha um filtro", ["Nenhum", "Escala de Cinza", "Inversão de Cores", "Aumento de Contraste", "Desfoque (Blur)", "Nitidez (Sharpen)", "Detecção de Bordas"])
    valor_filtro = st.slider("Valor do filtro", 0.1, 3.0, 1.5, step=0.1) if filtro == "Aumento de Contraste" else None

    transform = st.selectbox("Escolha uma transformação", ["Nenhuma", "Rotação 90°", "Rotação 180°", "Rotação 270°", "Espelhar Horizontalmente", "Espelhar Verticalmente", "Redimensionar"])
    valor_transform = st.slider("Valor da escala", 0.1, 2.0, 0.5, step=0.1) if transform == "Redimensionar" else None

#botão aplicar
    if st.button("Aplicar"):
        img_result = aplicar_filtro(image_cv, filtro, valor_filtro) if filtro != "Nenhum" else image_cv
        img_result = aplicar_transformacao(img_result, transform, valor_transform) if transform != "Nenhuma" else img_result

        if len(img_result.shape) == 2:
            st.image(img_result, caption="Imagem Processada", channels="GRAY", use_column_width=True)
            img_result = cv2.cvtColor(img_result, cv2.COLOR_GRAY2RGB)
        else:
            st.image(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB), caption="Imagem Processada", use_column_width=True)

        byte_im = salvar_para_download(img_result)
        st.download_button(label="📥 Baixar imagem", data=byte_im, file_name="imagem_processada.png", mime="image/png")
