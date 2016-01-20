__author__ = 'Chris Simmons'

import cv2
import numpy as np
from PIL import Image
from scipy import signal as sp

#i,j is a sift feature point (col --288,row --384 )  i is col, j is row
def get_pixel_window(i,j,image):

    window = np.zeros((15,15))

    im = Image.open(image)
    im2 = im.convert('L')
    im_read = im2.load()

    w,h = im.size
    # w = 384
    # h = 288

    col = 7
    row = 7

    #j,i is col,row, want im_read

    window[col][row] = im_read[i,j]

    q = 7

    for m in range(15):
        v = 7
        for n in range(15):
            if (i-q) < 0:
                window[m][n] = 0

            elif (i-q) >= w:
                window[m][n] = 0

            elif (j-v) >= h:
                window[m][n] = 0

            else:
                try:
                    window[m][n] = im_read[i - q, j - v]
                except:
                    print i, j
                    print i-q
                    print j - v
                    quit()
            v -= 1
        q -= 1

    #print window
    #quit()

    return window

#x,y is col,row
#p,q is col,row
def normal_cross(x,y,p,q,image1,image2):

    img2 = cv2.imread(image2)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    h,w = gray2.shape

    #h rows
    #w is col

    cross_correlation_values = {}

    img2_col = 7
    window_1 = get_pixel_window(x,y,image1)
    window_2 = get_pixel_window(img2_col,q,image2)

    num = 0
    left_den = 0
    right_den = 0

    while img2_col < w - 7:
        #normalized correlation
        for m in range(15):
            for n in range(15):
                num += (window_1[m,n] - window_2[m,n])**2
                left_den += (window_1[m,n])**2
                right_den += (window_2[m,n])**2

        norm_corr = num / np.sqrt(left_den*right_den)
        cross_correlation_values[(img2_col,q)] = norm_corr
        img2_col += 1

    min_pt = min(cross_correlation_values, key = cross_correlation_values.get)

    return min_pt

