import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregue a imagem em tons de cinza
imagem = cv2.imread('raposa.png', cv2.IMREAD_GRAYSCALE)

# Encontre os contornos na imagem
contornos, _ = cv2.findContours(imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crie uma cópia da imagem original para desenhar os contornos
imagem_contornos = imagem.copy()

# Desenhe os contornos na imagem original
cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2) 

# Exiba a imagem original com os contornos
plt.figure(figsize=(12, 6))

# Imagem original
plt.subplot(121)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Imagem com os contornos
plt.subplot(122)
plt.imshow(cv2.cvtColor(imagem_contornos, cv2.COLOR_BGR2RGB))
plt.title('Imagem com Contornos')
plt.axis('off')

plt.show()