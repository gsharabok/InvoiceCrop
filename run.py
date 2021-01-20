from __future__ import print_function
from builtins import input
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import ndimage
import argparse

######### Change file path here
file =  r'sample_image.jpg'
#########

linelen = 0
version = 2

im1 = cv2.imread(file, 0)
im = cv2.imread(file)

h_im, w_im, c_im = im.shape
linelen = 100 #h_im/2

ret,thresh_value = cv2.threshold(im1,180,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)

#rotation
def rotate(img, linelen):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=5)
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=linelen, maxLineGap=5) #minLineLength=100

    angles = []

    i = 0   
    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            if (linelen > 300):
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 1)
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            angles.append(angle)

    median_angle = np.median(angles)
    if (median_angle != 0):
        median_angle += 0.2
    img_rotated = ndimage.rotate(img, median_angle)

    print("Angle is {}".format(median_angle))
    return img_rotated


im = rotate(im, linelen)

# Apply Gamma=2.0 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_two_point_two = np.array(255*(im/255)**2.0,dtype='uint8')
im = gamma_two_point_two

gray = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)[..., 0]


clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(32,32))
contrast = clahe.apply(gray)
ret, thresh = cv2.threshold(contrast, 20, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

if(h_im > 1000):
    im = th3

contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cordinates = []
maxh = 0
maxh2 = 0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cordinates.append((x, y, w, h))
    
    if (h > maxh):
        if (maxh != 0):
            maxh2 = maxh
            maxcnt2 = maxcnt
        maxh = h
        maxcnt = cnt
    elif (h > maxh2):
        maxh2 = h
        maxcnt2 = cnt    

x,y,w,h = cv2.boundingRect(maxcnt)

crop_img = im[y:y + h, x:x + w]
if(h_im > 700 or w_im > 500):
    crop_img = cv2.fastNlMeansDenoising(crop_img, None, 25, 7, 21)

cv2.imwrite('res1.jpg', crop_img)

if (maxh2 == maxh or maxh2 == maxh - 1):
    x,y,w,h = cv2.boundingRect(maxcnt2)
    crop_img1 = im[y:y + h, x:x + w]
    crop_img1 = cv2.fastNlMeansDenoising(crop_img1, None, 20, 7, 21)
    cv2.imwrite('res2.jpg', crop_img1)