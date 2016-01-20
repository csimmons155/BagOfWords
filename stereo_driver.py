__author__ = 'christophersimmons'
import cv2
import numpy as np
from stereo_matching import *

image1 = "scene_l.bmp"
image2 = "scene_r.bmp"
img1 = cv2.imread(image1,0)
img2 = cv2.imread(image2,0)

#the depth image
outimg = np.zeros((len(img2),len(img2[0])))

temps_img1 = {}
temps_img2 = {}

for x in range(0,len(img1)):
    for y in range(0,len(img1[0])):
        if x > 7 and x < len(img1) - 8 and y > 7 and y < len(img1[0]):
            for p in range(0,len(img2)):
                for q in range(0,len(img2[0])):
                    if p > 7 and p < len(img1) - 8 and q > 7 and q < len(img1[0]):
                        col2,row2 = normal_cross(y,x,q,p,image1,image2) #col,row
                        test = 255 - (5 * int(((40000.0/col2 - (y)) / 40000.0)*255.0))
                        #print x,y
                        outimg[x][y] = 255 - (5 * int(((40000.0/col2 - (y)) / 40000.0)*255.0))





