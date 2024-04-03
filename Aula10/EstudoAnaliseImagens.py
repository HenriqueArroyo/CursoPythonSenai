import cv2
# Carregar uma imagem usando OpenCV
imagem_opencv = cv2.imread('Aula10/imagem.png')

# Exemplo usando PIL:
from PIL import Image
# Abrir uma imagem usando PIL
imagem_pil = Image.open('Aula10/imagem.png')

# Redimensionar a imagem usando OpenCV
imagem_redimensionada_opencv = cv2.resize(imagem_opencv, (100, 100))

# Rotacionar a imagem usando PIL
imagem_rotacionada_pil = imagem_pil.rotate(45)