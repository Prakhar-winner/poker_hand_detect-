# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:45:03 2025

@author: prakh
"""

from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
result = model('F:\PRO\Running Yolo\istockphoto-1338736300-612x612.jpg', show=True)
cv2.waitKey(0)