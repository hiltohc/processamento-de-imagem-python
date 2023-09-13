import cv2
import numpy as np
import matplotlib.pyplot as plt

# imagem cinza
imagem = cv2.imread('raposa.png', cv2.IMREAD_GRAYSCALE)

# detecção de bordas
b_sobel = cv2.Sobel(imagem, cv2.CV_64F, 1, 1, ksize=5)

# Exiba a imagem de bordas resultante
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(imagem, cmap='gray')
plt.axis('off')
plt.title("original")

plt.subplot(122)
plt.imshow(np.abs(b_sobel), cmap='gray')
plt.axis('off')
plt.title("Imagem resultante")

plt.show()



