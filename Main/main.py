import analisaQR
import analiseDeBandeiras
import frameDetection
import cv2

#Decolar - Movimentação
print("M: Decolando drone...") 
#Leitura QR
print("Lendo o QRCode...")

qr = 'QRCode\\imagens\\brasil.png' #Recebe o endereço da imagem do QRCode desejado
codigo = analisaQR.decodificaQR(qr) #Analisa ele e retorna o código referente
#Movimentação

#FRAMEDETECTION
# Declarando e convertendo a Imagem 
imagemParam = cv2.imread("FrameDetection\\frame.png")

# Configurando os elementos
bebop = frameDetection.Drone(0, 0, 0, 100, 0.1, 0.3, 0)
frame = frameDetection.RecognitionFrame(imagemParam)

# Criando o objeto a ser analisado 
objeto = frameDetection.RecognitionFrame(imagemParam)

# Faz a máscara e converte para cinza
objeto.execute()

# Achando os contornos da imagem
countours = objeto.contoursRecognition()

# Mensurando os contornos da imagem
x, y, w, h = cv2.boundingRect(countours[0])

objeto.result()

print("({}, {})   Largura = {}   Altura = {}".format(x, y, w, h))

#Movimentação
frameX = x + w/2
frameY = y + h/2

imageX, imageY, _ = imagemParam.shape
imageX = imageX/2
imageY = imageY/2

#M é utilizado para representar movimentação
if frameX < imageX:
    print('M: Voa para direita')
else:
    print('M: Voa para esquerda')
if frameY < imageY:
    print('M: Voa para cima')
else:
    print('M: Voa para baixo')

#Bandeiras
analiseDeBandeiras.identificaBandeira(codigo) #Utiliza o código do identificado do QRCode para buscar a bandeira desejada

#Movementação - Pousar
print("Seguindo em frente...")
print("Pousando...")