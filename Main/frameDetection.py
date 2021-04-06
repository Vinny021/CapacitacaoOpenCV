import cv2
import numpy as np


class RecognitionFrame:
    def __init__(self, frame):
        self.frame = frame
        self.frameOriginal = frame
        self.lower_red1 = (0, 140, 100)
        self.upper_red1 = (10, 255, 255)
        self.lower_red2 = (170, 50, 100)
        self.upper_red2 = (180, 255, 255)

    def get_frame(self):
        return self.frame

    def execute(self):
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        redMask1 = cv2.inRange(self.frame, self.lower_red1, self.upper_red1)
        redMask2 = cv2.inRange(self.frame, self.lower_red2, self.upper_red2)

        result1 = cv2.bitwise_and(self.frame, self.frame, mask = redMask1)
        result2 = cv2.bitwise_and(self.frame, self.frame, mask = redMask2)

        result = cv2.bitwise_or(result1, result2)

        kernel = np.ones((70, 70), np.uint8)
        dilation = cv2.dilate(result, kernel, iterations=1)

        kernel = np.ones((75, 75), np.uint8)
        self.frame = cv2.erode(dilation, kernel, iterations=1)

        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_HSV2BGR)
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("teste1", self.frame)
        #cv2.waitKey(0)

        self.contoursRecognition()

    def contoursRecognition(self):
        self.contours, _ = cv2.findContours(self.frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(self.frame, self.contours, -1, (0, 0, 255), 3)

        #cv2.imshow("teste2", self.frame)
        #cv2.waitKey(0)

        x, y, w, h = cv2.boundingRect(self.contours[0])
        cv2.rectangle(self.frameOriginal, (x, y), (x + w, y + h), (0,255,0), 3)
        #cv2.imshow("teste3", self.frameOriginal)
        #cv2.waitKey(0)

        return self.contours

    def result(self):
        cv2.imshow("result", self.frameOriginal)
        cv2.waitKey(0)

class Movimentation:
    def __init__(self):
        pass

    def SOBE():
        print('Subiu.')
        pass

    def DESCE():
        print('Desceu.')
        pass

    def FRENTE():
        print('Foi para frente.')
        pass

    def TRAS():
        print('Foi para tras.')
        pass

    def ROLL_ESQ():
        print('Inclinou para esquerda.')
        pass

    def ROLL_DIR():
        print('Inclinou para direita.')
        pass

    def YAW_ESQ():
        print('Virou para esquerda.')
        pass

    def YAW_DIR():
        print('Virou para direita.')
        pass

    def Takeoff():
        print('Saiu do chão.')
        pass

    def Landing():
        print('Pousou.')
        pass

    
    def goto(self, Drone, RecognitionFrame):
        dronex, droney = Drone.centerPoint
        framex, framey = RecognitionFrame.centerPoint

        if dronex >= framex:
            self.YAW_ESQ()
        
        else:
            self.YAW_DIR()


        if droney >= framey:
            self.SOBE()
        
        else:
            self.DESCE()
            

class Drone:
    def __init__(self, positionx, positiony, positionz, battery, height, width, centerPoint):
        self.positionx = positionx
        self.positiony = positiony
        self.positionz = positionz
        self.battery = battery
        self.height = height
        self.width = width
        self.centerPoint = centerPoint

    def get_positionX(self):
        return self.positionx

    def get_positionY(self):
        return self.positiony

    def get_positionZ(self):
        return self.positionz

    def get_battery(self):
        return self.battery

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_centerPoint(self, RecognitionFrame):
        self.centerPoint = (frame.shape[0]/2), (frame.shape[1]/2)  
        return self.centerPoint


