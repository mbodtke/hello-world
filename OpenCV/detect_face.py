# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 23:35:57 2018

@author: mbodtke
"""


import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) &0xff
    if k==27:
        break

capture.release()
cv2.destroyAllWindows()   