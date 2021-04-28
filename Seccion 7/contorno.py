from cv2 import cv2

imgPath = "C:/Users/franc/Downloads/Curso Python - De 0 hasta reconocimiento facial/Seccion 7/contorno.jpg"

img = cv2.imread(imgPath)
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
contornos, jerarquias = cv2.findContours(
    umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contornos, -1, [65, 105, 225], 3)
# Mostrar
cv2.imshow("Imagen original", img)
# cv2.imshow("Imagen en grises", grises)
# cv2.imshow("Imagen Umbral", umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
