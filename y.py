#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 13:39:53 2025

@author: velibilir
"""

import torch
import cv2

# Modeli yükle
model = torch.hub.load('ultralytics/yolov5', 'custom', path='trafik_model.pt')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Tahmin yap
    results = model(frame)
    results.print()
    frame = results.render()[0]

    cv2.imshow("Traffic Sign Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()