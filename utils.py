import io
from PIL import Image
import cv2

def salvar_para_download(image_cv):
    image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
    result_pil = Image.fromarray(image_rgb)
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    return buf.getvalue()
