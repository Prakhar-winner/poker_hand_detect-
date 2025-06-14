# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:17:58 2025

@author: prakh
"""


import cv2
import cvzone
from ultralytics import YOLO
import math
import PockerHand

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO('playingCards.pt')


classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']

hand = []
while True:
    success, img = cap.read()
    result = model(img,stream=True)
    hand = []
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            w = x2-x1
            h = y2-y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil(box.conf[0]*100)/100

            cls = int(box.cls[0])
            cvzone.putTextRect(q, f'{classNames[cls]}{conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

            if conf>0.5:
                hand.append(classNames[cls])

    hand=list(set(hand))

    if len(hand) == 5:
        result = PockerHand.FindPockerHand(hand)
        print(result)
        cvzone.putTextRect(img, f'Your Hand:{result}', (150,50), scale=2, thickness=5)

    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break