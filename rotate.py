import os
import cv2
import imutils


def rotateSet(dirStart,folder,imgMiddle,dirCounter=1):
    while os.path.isdir(dirStart + str(dirCounter)):
        imgCounter = 1
        imgStart = "-0000"
        imgPath = dirStart + str(dirCounter) + imgMiddle + str(dirCounter) + imgStart + str(imgCounter) +".png"
        while os.path.isfile(imgPath):
            angle = (imgCounter % 4) * 90
            img = cv2.imread(imgPath)
            rotated = imutils.rotate_bound(img, angle)
            cv2.imwrite(imgPath,rotated)

            if imgCounter == 9:
                imgStart = "-000"
            if imgCounter == 99:
                imgStart = "-00"

            #update imagePath
            imgCounter+=1
            imgPath = dirStart + str(dirCounter) + imgMiddle + str(dirCounter) + imgStart + str(imgCounter) +".png"
        
        if dirCounter == 9:
            dirStart = f'RotatedEnglish/Img/{folder}/Bmp/Sample0'
            imgMiddle = "/img0"
        
        dirCounter+=1

rotateSet("RotatedEnglish/Img/GoodImg/Bmp/Sample00","GoodImg","/img00")
rotateSet("RotatedEnglish/Img/BadImag/Bmp/Sample00","BadImag","/img00")