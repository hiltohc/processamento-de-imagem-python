import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('raposa1.jpg')

# filtro Gaussiano
imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)  

plt.figure(figsize=(12, 6))

# Imagem original
plt.subplot(121)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

# Imagem suavizada
plt.subplot(122)
plt.imshow(cv2.cvtColor(imagem_suavizada, cv2.COLOR_BGR2RGB))
plt.title('Filtro Gaussiano')
plt.axis('off')

plt.show()