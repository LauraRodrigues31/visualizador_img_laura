import cv2
import numpy as np

def aplicar_filtro(image, filtro, value=None):
    if image is None:
        return None

    img = image.copy()

    if filtro == "Escala de Cinza":
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filtro == "Inversão de Cores":
        return cv2.bitwise_not(img)
    elif filtro == "Aumento de Contraste":
        factor = float(value) if value else 1.5
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255).astype(np.uint8)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    elif filtro == "Desfoque (Blur)":
        return cv2.GaussianBlur(img, (5, 5), 0)
    elif filtro == "Nitidez (Sharpen)":
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        return cv2.filter2D(img, -1, kernel)
    elif filtro == "Detecção de Bordas":
        return cv2.Canny(img, 100, 200)
    return img
