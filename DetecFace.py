#!/usr/bin/env python
#coding=utf-8
import os
from PIL import Image, ImageDraw
# import cv

from cv2 import cv

def detect_object(image):
    '''检测图片，获取人脸在图片中的坐标'''
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    cascade = cv.Load("E:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml")
    rect = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage(), 1.1, 3,
        cv.CV_HAAR_DO_CANNY_PRUNING, (40,40))

    result = []
    for r in rect:
        result.append((r[0][0], r[0][1], r[0][0]+r[0][2], r[0][1]+r[0][3]))

    return result

def process(infile):
    '''在原图上框出头像并且截取每个头像到单独文件夹'''
    image = cv.LoadImage(infile)
    # if image:
    faces = detect_object(image)
    if faces:
        # save_dir = infile.split('.')[0]+"_faces"
        # os.mkdir(save_dir)
        count = 0
        for (x1,y1,x2,y2) in faces:
            file_name = infile + '.jpg'
            # file_name = os.path.join(infile,str(count)+".jpg")
            Image.open(infile).convert('RGB').crop((x1,y1,x2,y2)).save(file_name)
            count+=1
            img1 = cv.LoadImage(file_name)
            re_img = cv.CreateImage((48, 48),8, 3)
            cv.Resize(img1, re_img, cv.CV_INTER_LINEAR)
            cv.SaveImage(file_name, re_img)

if __name__ == "__main__":
    process("./KA.AN1.39.tiff")