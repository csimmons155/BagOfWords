__author__ = 'christophersimmons'
import cv2
import math
import numpy as np

def get_features(image1):

    img1 = cv2.imread(image1)
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(gray1,None)

    return des, des.shape[0]


def get_kmeans(features):

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret,label,center = cv2.kmeans(features,1000,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    return ret,label,center


def get_train_histogram(scene_class, label):

    histogram = {}

    for key in scene_class:
        val = [0 for x in range(1000)]
        first, last = scene_class[key][0], scene_class[key][1]
        for i in range(first,last+1):
            val[label[i]] += 1
        histogram[key] = val

    return histogram

def get_test_historgram(test_features,center):

    histogram = {}

    for key in test_features:
        val = [0 for x in range(1000)]
        for row in test_features[key]:
            val[get_nearest_neighbor(row,center)] += 1

        histogram[key] = val
        #print key, val[0:3]

    return histogram

def get_nearest_neighbor(feature, center):

    for row in range(len(center)):
        min_dis = 10000000 #random large number
        min_row = 0
        dis = 0
        for col in range(len(center[row])):
            #print feature[col]
            #print center[row][col]
            dis += math.fabs(feature[col] - center[row][col])
        if dis < min_dis:
            min_dis = dis
            min_row = row
    #print "this min row"+min_row
    return min_row

def mapping(train_hist, test_hist):

    all_train_hist = []

    n = 0
    map = {}

    matches = {}


    for key in train_hist:
        emp = []
        for j in train_hist[key]:
            emp.append(j)
        all_train_hist.append(emp)
        map[n] = key
        n += 1

    for i in test_hist:
        near = map[get_nearest_neighbor(test_hist[i], all_train_hist)]
        print i, near
        matches[i] = near

    return matches




#get_features("scene_l.bmp")





