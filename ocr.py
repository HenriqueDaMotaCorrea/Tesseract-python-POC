import cv2
import pytesseract


def get_string(img_path):
    # Read image using opencv
    img = cv2.imread(img_path)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang="eng")
    return result

imagem = input("Caminho da imagem de entrada: ")
print('========================================\n')
print(get_string(imagem))
print('\n========================================')
