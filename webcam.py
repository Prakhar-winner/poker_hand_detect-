# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:47:51 2025

@author: prakh
"""

import cv2
import cvzone
from ultralytics import YOLO
import math

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 380)

className = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag","tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

model = YOLO('../Yolo-Weights/yolov8n.pt')
while True:
    success, img = cap.read()
    result = model(img,stream=True)

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
            cvzone.putTextRect(img, f'{className[cls]}{conf}', (max(0, x1), max(35, y1)), scale=2, thickness=2)


    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break