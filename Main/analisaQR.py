import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decodificaQR(frame):

    qr = cv2.imread(frame)

    for barcode in decode(qr): 
        identificacao = barcode.data.decode('utf-8')

        frame = np.array([barcode.polygon], np.int32)
        frame = frame.reshape((-1, 1, 2))
        
        cv2.polylines(qr, [frame], True, (0, 255, 0), 4)

    cv2.imshow('QRCode', qr)
    cv2.waitKey(0)
    
    identificacao = int(identificacao)
    return identificacao
    