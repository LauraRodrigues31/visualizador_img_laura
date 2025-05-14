import cv2

def aplicar_transformacao(image, transform, value=None):
    if image is None:
        return None

    img = image.copy()

    if transform == "Rotação 90°":
        return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif transform == "Rotação 180°":
        return cv2.rotate(img, cv2.ROTATE_180)
    elif transform == "Rotação 270°":
        return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif transform == "Espelhar Horizontalmente":
        return cv2.flip(img, 1)
    elif transform == "Espelhar Verticalmente":
        return cv2.flip(img, 0)
    elif transform == "Redimensionar":
        scale = float(value) if value else 0.5
        height, width = img.shape[:2]
        new_size = (int(width * scale), int(height * scale))
        return cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

    return img
