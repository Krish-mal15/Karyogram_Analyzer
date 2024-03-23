import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy
import math

img = cv2.imread("testData/k2-female-DS.jpeg")
#img = cv2.imread("testData/k1-male-cancer.png")
#img = cv2.imread("testData/k5-male.png")
#img = cv2.imread("testData/k6-female-turner.png")
#img = cv2.imread("testData/k7-female.png")
#img = cv2.imread("testData/k8-male-klinefelter.png")

# 660 x 430

colorFinder = ColorFinder(False)

hsvVals = {"hmin": 0, "smin": 0, "vmin": 0, "hmax": 0, "smax": 0, "vmax": 220}

imgColor, mask = colorFinder.update(img, hsvVals)

imgContours, contours, number = cvzone.findContours(img, mask, minArea=100)

#print(len(contours))

cv2.imshow('ImgColor', imgContours)
cv2.imshow('Mask', mask)

def diagnose():
    num = len(contours)

    if num <= 30:
        print("Number of chromosomes: N/A")
    else:
        print("Number of chromosomes: ", num)

    if num == 46 and number == 2:
        return "Normal"
    if num == 47 and number == 2:
        return "Down Syndrome"
    if num == 47 and number == 3:
        return "Klinefelter Syndrome"
    if num == 45 and number == 1:
        return "Turner's Syndrome"
    if num >= 50 or num <= 40:
        return "Cancer"

print("Diagnosis: ", diagnose())

cv2.destroyAllWindows()