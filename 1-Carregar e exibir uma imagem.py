import cv2

# Carregar a imagem
imagem = cv2.imread("raposa.png",0)


# Exibir a imagem
cv2.imshow("Imagem da raposa", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
