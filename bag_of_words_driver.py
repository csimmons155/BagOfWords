__author__ = 'christophersimmons'

import numpy as np
import os
import cv2
from bag_of_words import *
import time
import sys

root_dir = '.'

feature_count = 0
total_features = {}
n = 0
scene_class = {}
try:
    for (dirpath, dir, file) in os.walk(root_dir):
        if len(dir) != 0 and dir[0] != "images":
            for i in range(len(dir)):
                cur_dir = dirpath + dir[i]
                for(cur_dir,dir[i],files) in os.walk('./images/'+dir[i]):
                    for i in files:
                        if i == ".DS_Store":
                            pass
                        else:
                            #im = cv2.imread(cur_dir+'/'+i)
                            im = str((cur_dir+'/'+i))
                            if i == "images-1.jpeg" or i == "images-2.jpeg":
                                pass
                            else:
                                feature_array, amount = get_features(im)
                                feature_count += amount
                                for row in feature_array:
                                    total_features[n] = row
                                    if cur_dir in scene_class:
                                        scene_class[cur_dir].append(n)
                                    else:
                                        scene_class[cur_dir] = [n]
                                        #print cur_dir
                                    n += 1

except AttributeError:
    pass


range_scene_class = {}
for k in scene_class.keys():
    range_scene_class[k] = [min(scene_class[k]),max(scene_class[k])]

#print range_scene_class


features = np.ndarray((feature_count,128))
features = np.float32(features)

for x in range(0,feature_count):
    features[x] = total_features[x]


#print feature_count
#print features
start_time = time.time()
ret,label,center = get_kmeans(features)
print ("-----Kmeans Runtime: %s sec-----" % (time.time() - start_time))


start_time = time.time()
train_hist = get_train_histogram(range_scene_class,label)
print ("-----Train Histogram Runtime: %s sec-----" % (time.time() - start_time))



#######TEST IMAGES######



tol_test_features = {}
test_count = 0
count_per_img = {}
try:
    for (dirpath, dir, file) in os.walk(root_dir):
        if len(dir) != 0 and dir[0] != "images":
            for i in range(len(dir)):
                cur_dir = dirpath + dir[i]
                for(cur_dir,dir[i],files) in os.walk('./images/'+dir[i]):
                    #pic_dec = []
                    for i in files:
                        pic_dec = []
                        if i == ".DS_Store":
                            pass
                        else:
                            #im = cv2.imread(cur_dir+'/'+i)
                            im = str((cur_dir+'/'+i))

                            if i == "images-1.jpeg" or i == "images-2.jpeg":
                                feature_array, amount = get_features(im)
                                test_count += 1
                                #feature_count += amount
                                cnt = 0
                                for row in feature_array:
                                    row_new = (row)
                                    cnt += 1
                                    pic_dec.append(row_new)
                                tol_test_features[(cur_dir+'/'+i)] = pic_dec
                                count_per_img[(cur_dir+'/'+i)] = cnt
                                    #if row in center:
                                     #   center_count += 1
                            else:
                                pass


except AttributeError:
    pass

#print tol_test_features
test_features = {}

#perhaps unnessessary for loop
for key in tol_test_features:
    for key2 in count_per_img:
        if key2 == key:
            test_matrix = np.ndarray((count_per_img[key2],128))
            test_matrix = np.float32(test_matrix)
            t = 0
            for row in tol_test_features[key]:
                test_matrix[t] = row
                t += 1
            test_features[key] = test_matrix

start_time = time.time()
test_hist = get_test_historgram(test_features,center)
print ("-----Test Histogram Runtime: %s sec-----" % (time.time() - start_time))

start_time = time.time()
match = mapping(train_hist,test_hist)
print ("-----Matching Runtime: %s sec-----" % (time.time() - start_time))



