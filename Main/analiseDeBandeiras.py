import cv2
import numpy as np

# Interpretar o QR (descobrir a bandeira à analisar)

# Separar as bandeiras
imagemArgentina = cv2.imread('Analise-bandeiras\\images\\argentina.png')
imagemBrasil = cv2.imread('Analise-bandeiras\\images\\brasil.jpg')
imagemChile = cv2.imread('Analise-bandeiras\\images\\chile.jpg')

def identificaBandeira(qr):
    for i in range(0, 3):

        if(i == 0):
            imagemLida = imagemArgentina
            print("Olhando para a bandeira da Argentina")
        elif(i == 1):
            imagemLida = imagemBrasil
            print("Olhando para a bandeira da Brasil")
        elif(i == 2):
            imagemLida = imagemChile
            print("Olhando para a bandeira do Chile")

        

        if(qr == 5522):
            ok = bandeiraBrasil(imagemLida) 
        elif(qr == 5318):
            ok = bandeiraArgentina(imagemLida)
        elif(qr == 5418):
            ok = bandeiraChile(imagemLida)

        if(ok == 1):
            return 
        

def bandeiraBrasil(imagemLida):
    brasilHSV = cv2.cvtColor(imagemLida, cv2.COLOR_BGR2HSV)

    verdeMin = (45, 100, 100)
    verdeMax = (80, 255, 255)

    verde = cv2.inRange(brasilHSV, verdeMin, verdeMax)
    
    resultado = cv2.bitwise_and(imagemLida, imagemLida, mask = verde)
    cv2.imshow('result', resultado)
    cv2.waitKey(0)

    pixeisVerdes = 0
    pixeisTotais = 0
    for i in verde:
        for j in i: 
            pixeisVerdes+=j
            pixeisTotais+=1

    pixeisVerdes = pixeisVerdes/255
    porcentagem = pixeisVerdes / pixeisTotais 
    
    if(porcentagem < 0.50):
        print("M: Não é a bandeira do Brasil")
        return 0
    else:
        print("Essa é a bandeira do Brasil")
        return 1


def bandeiraArgentina(imagemLida):
    argentinaHSV = cv2.cvtColor(imagemLida, cv2.COLOR_BGR2HSV)

    azulMin = (80, 90, 100)
    azulMax = (130, 255, 255)

    azul = cv2.inRange(argentinaHSV, azulMin, azulMax)
    resultado = cv2.bitwise_and(imagemLida, imagemLida, mask = azul)
    cv2.imshow('result', resultado)
    cv2.waitKey(0)

    qtd_azul = 0
    qtd_total = 0

    for i in azul:
        for j in i:
            qtd_azul += j
            qtd_total +=1
    
    qtd_azul = qtd_azul / 255

    porcentagem = qtd_azul/qtd_total

    if(porcentagem < 0.50):
        print("Não é a bandeira da Argentina")
        print("M: Voa para direta")
        return 0
           
    else:
        print("Essa é a bandeira da Argentina")
        return 1
            

def bandeiraChile(imagemLida):
    chileHSV = cv2.cvtColor(imagemLida, cv2.COLOR_BGR2HSV)

    vermelhoMin1 = (0, 50, 200)
    vermelhoMax1 = (10, 255, 255)
    vermelhoMin2 = (160, 50, 200)
    vermelhoMax2 = (179, 255, 255)

    vermelho1 = cv2.inRange(chileHSV, vermelhoMin1, vermelhoMax1)
    vermelho2 = cv2.inRange(chileHSV, vermelhoMin2, vermelhoMax2)
    
    vermelho = cv2.add(vermelho1, vermelho2)

    resultado = cv2.bitwise_and(imagemLida, imagemLida, mask = vermelho) 
    cv2.imshow('result', resultado)
    cv2.waitKey(0) 

    pixeisVermelhos = 0
    pixeisTotais =0

    for i in vermelho:
        for j in i: 
            pixeisVermelhos+=j
            pixeisTotais+=1

    pixeisVermelhos = pixeisVermelhos / 255
    porcentagem = pixeisVermelhos / pixeisTotais 
    
    if(porcentagem < 0.40):
        print("Não é a bandeira do Chile")
        print("M: Voa para direta")
        return 0
    else:
        print("Essa é a bandeira do Chile")
        return 1



# Receber a imagem da câmera (de novo)
# Analisar as bandeiras
