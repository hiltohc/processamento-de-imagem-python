import cv2
import matplotlib.pyplot as plt

#imagem colorida
imagem1 = cv2.imread('raposa1.jpg')

# Converter para cinza
imagem2 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)

# exibir ambas as imagens
plt.figure(figsize=(8, 4))

# Imagem colorida
plt.subplot(121)
plt.imshow(cv2.cvtColor(imagem1, cv2.COLOR_BGR2RGB))
plt.title('Imagem Colorida')
plt.axis('off')

# Imagem cinza
plt.subplot(122)
plt.imshow(imagem2, cmap='gray')
plt.title('Imagem Cinza')
plt.axis('off')

plt.show()