import os, cv2, glob
import numpy as np
import imageio
import imgaug as iaa
from imgaug import augmenters as ia
from pullImagesToFolder import cDict

home = os.getcwd()
collages = os.getcwd() + '/collages/'
baseImages = os.getcwd() + '/baseImages/'
cardDict = cDict()


def createCollageFolders():

    if not os.path.isdir(collages):
        os.mkdir(collages)
        print('Created collage folder\n')
    else:
        print('Collage folder exists\n')

    os.chdir(collages)

    for ids, names in cardDict.items():
        if not os.path.isdir(os.path.join(collages, str(cardDict.get(ids)))):
            os.makedirs(os.path.join(collages, str(cardDict.get(ids))))
            print('Created the collage image folder')


createCollageFolders()

pic = []
resize = [421, 614]




#
# def read2Folders(curr):
#     pics = []
#     resize = [421, 614]
#     size = [1024, 1024]
#
#     for i in range(2):
#         for img in glob.glob(basePath+imagePath[curr+i]+'/*.jpg'):
#             n = cv2.imread(img)
#             fix = cv2.resize(n,resize,interpolation=cv2.INTER_AREA)
#             pics.append(fix)
#     horizontal1 = np.hstack([pics[1],pics[0],pics[2]])
#     horizontal2 = np.hstack([pics[4],pics[3],pics[5]])
#
#     fix = np.vstack([horizontal1,horizontal2])
#     collage = cv2.resize(fix, size, interpolation=cv2.INTER_AREA)
#
#     return collage
#
#
# for j in range(int((len(imagePath))/2)):
#     image = read2Folders(j*2)
#     cv2.imwrite(destPath + '%d'%j+'.jpg', image)
