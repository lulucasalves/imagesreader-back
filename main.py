import cv2
import pytesseract
import matplotlib.pyplot as plt

# Carregue a imagem
image = cv2.imread('images/1.png')

# Defina as coordenadas da ROI (x, y, largura, altura)
roi_coordinates = (100, 927, 350, 200)  # Exemplo: ROI começa em (100, 100) e tem largura 300 e altura 200

# Extraia a ROI da imagem
x, y, width, height = roi_coordinates
roi = image[y:y+height, x:x+width]

# Desenhe um retângulo na imagem original para mostrar a ROI
cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)  # (0, 255, 0) representa a cor verde, 2 é a espessura da linha

# Converta a ROI para escala de cinza (opcional, dependendo da imagem)
roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Execute o reconhecimento de texto com o Tesseract
text = pytesseract.image_to_string(roi_gray, lang='por')

# Imprima o texto extraído
print(text.split('\n'))

# Mostrar a imagem com o retângulo usando o matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imagem com ROI')
plt.axis('off')
plt.show()


