#!/usr/bin/env python
#coding=utf-8
import os
from PIL import Image, ImageDraw
import cv2

from cv2 import cv

def detect_object(image):
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    cascade = cv.Load("./model/haarcascade_frontalface_alt_tree.xml")
    rect = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage(), 1.1, 3,
        cv.CV_HAAR_DO_CANNY_PRUNING, (40,40))
    # 获取坐标并记录
    result = []
    for r in rect:
        result.append((r[0][0], r[0][1], r[0][0]+r[0][2], r[0][1]+r[0][3]))

    return result

# 将坐标中的矩形画出
def ontime_process(image):
    face = detect_object(image)
    if face:
        for x1,y1,x2,y2 in face:
            cv2.cv.Rectangle(image, (x1,y1), (x2,y2), (0, 255, 0))
    return image

# 测试代码
def test_ontime_process(file_path):
    img = cv2.cv.LoadImage(file_path)
    img = ontime_process(img)
    cv2.cv.ShowImage('aa',img)
    cv2.cv.WaitKey(0)

# 将矩形区域截取出来然后缩放到48*48
def process(infile):
    image = cv.LoadImage(infile)
    # if image:
    faces = detect_object(image)
    if faces:
        # 本项目中严格控制一张图片只有一个人脸，所以以下循环直接return
        for (x1,y1,x2,y2) in faces:
            file_name = infile + '.jpg'
            Image.open(infile).convert('RGB').crop((x1,y1,x2,y2)).save(file_name)
            img1 = cv.LoadImage(file_name)
            re_img = cv.CreateImage((48, 48),8, 3)
            cv.Resize(img1, re_img, cv.CV_INTER_LINEAR)
            cv.SaveImage(file_name, re_img)
            return infile + '.jpg'


if __name__ == "__main__":
    test_ontime_process('./KA.HA2.30.tiff')
    # process("./xx.png")