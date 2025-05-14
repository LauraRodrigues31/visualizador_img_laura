import io # é a biblioteca que permite dados em memoria que nem pedimos para salvar no disco
from PIL import Image
import cv2

#função que fala pra baixar a imagem png via streamlit
def salvar_para_download(image_cv):
    #img BGR para RGB
    image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
    result_pil = Image.fromarray(image_rgb)
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    return buf.getvalue()
