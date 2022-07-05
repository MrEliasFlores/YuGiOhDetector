import os
import cv2
import glob
import numpy as np

basePath = os.getcwd()+'/images/train/'
destPath = os.getcwd()+'/images/trainCollage/'

with open(basePath+'/trainLabel.txt') as f:
    imagePath = f.read().splitlines()

def read2Folders(curr):
    pics = []
    resize = [421, 614]
    size = [1024, 1024]

    for i in range(2):
        for img in glob.glob(basePath+imagePath[curr+i]+'/*.jpg'):
            n = cv2.imread(img)
            fix = cv2.resize(n,resize,interpolation=cv2.INTER_AREA)
            pics.append(fix)
    horizontal1 = np.hstack([pics[1],pics[0],pics[2]])
    horizontal2 = np.hstack([pics[4],pics[3],pics[5]])

    fix = np.vstack([horizontal1,horizontal2])
    collage = cv2.resize(fix, size, interpolation=cv2.INTER_AREA)

    return collage


for j in range(int((len(imagePath))/2)):
    image = read2Folders(j*2)
    cv2.imwrite(destPath + '%d'%j+'.jpg', image)
