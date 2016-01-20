__author__ = 'christophersimmons'
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




im1 = cv2.imread("scene_l.bmp", 0)
im2 = cv2.imread("scene_r.bmp",0)

out1 = np.zeros((len(im1),len(im2[0])))
out2 = np.zeros((len(im2),len(im2[0])))

f = open('3d_pointCloud.txt', 'w')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')


baseline = 100 #mm
focal = 400
point_cloud = ""

for x in range(7, len(im1) - 7):
    wind2 = im2[x-7:x+8, 0:len(im2[x])] #15x15 window for image 2
    for y in range(7, len(im1[0])-7):
        wind1 = im1[x-7:x+8, y-7:y+8]#15x15 window for image 1 at x,y
        res = cv2.matchTemplate(wind2,wind1,cv2.TM_CCORR_NORMED)
        #min_loc = best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #get the 3d point and depth image
        if y != max_loc[0]:
            y_max = max_loc[0]
            disparity = (y - y_max)
            z = (baseline*focal) / (disparity)
            out1[x,y] = disparity
            right_row = focal * (y/z)
            x1 = (baseline * (2*right_row)) / (2 * disparity)
            y1 = (baseline * (y + y_max)) / (2* disparity)
            f.write("("+str(x1)+","+str(y1)+","+str(z)+")\n")
            #Axes3D.plot(ax,x1,y1,zs=z)


cv2.imwrite("depth.bmp", out1)
f.close()