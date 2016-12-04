# -*- coding=utf-8 -*-
"""
@file ： extract_silhouettes_from_videos.py
@author : duanxxnj@163.com
@time : 11/30/16 3:55 AM
"""
import cv2
import os

"""
    the kernel used by open and close operation
"""
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))

for filename in os.listdir('./videos'):
    angle = filename.split('-')[-1].split('.')[0]
    if angle != '090':
        continue

    print filename
    videoCapture = cv2.VideoCapture('./videos/'+filename)
    fgbgMOG = cv2.createBackgroundSubtractorMOG2()
    fgbgKNN = cv2.createBackgroundSubtractorKNN()

    success, frame = videoCapture.read()

    while success:
        cv2.imshow('video', frame)

        f1 = fgbgKNN.apply(frame)
        ret, f1 = cv2.threshold(f1, 200, 255, cv2.THRESH_BINARY)
        cv2.morphologyEx(f1, cv2.MORPH_CLOSE, kernel2)
        cv2.morphologyEx(f1, cv2.MORPH_OPEN, kernel1)

        cv2.imshow('KNN', f1)

        f2 = fgbgMOG.apply(frame)
        ret, f2 = cv2.threshold(f2, 200, 255, cv2.THRESH_BINARY)
        cv2.morphologyEx(f1, cv2.MORPH_CLOSE, kernel2)
        cv2.morphologyEx(f1, cv2.MORPH_OPEN, kernel1)

        cv2.imshow('MOG', f2)

        ret, f3 = cv2.threshold(f1 + f2, 200, 255, cv2.THRESH_BINARY)
        cv2.morphologyEx(f1, cv2.MORPH_CLOSE, kernel2)
        cv2.morphologyEx(f1, cv2.MORPH_OPEN, kernel1)
        cv2.imshow('final', f3)
        cv2.waitKey(30)
        success, frame = videoCapture.read()
