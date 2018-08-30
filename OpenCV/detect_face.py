# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 23:35:57 2018

@author: mbodtke

First attempt at image detection by following sentdex tutorial on Haar Cascade Object Detection:
https://www.youtube.com/watch?v=88HdqNDQsEk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=16
"""


import cv2
import numpy as np

#create cascade classifier with pretrained data in .xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#setup webcam feed
capture = cv2.VideoCapture(0)

#start infinite loop
while True:
    ret, img = capture.read() #read single frame into img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #use classifier to detect faces in frame- optional paramaters blindly followed from tutorial
    for (x,y,w,h) in faces:  
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #draw rectangle around faces
    
    cv2.imshow('img',img) #show frame (will include rectangle if faces is non empty)
    k = cv2.waitKey(30) &0xff
    if k==27:  #'Esc' key to break the infinite loop
        break

capture.release() #release webcam
cv2.destroyAllWindows()   #destroy window created from cv2.imshow
