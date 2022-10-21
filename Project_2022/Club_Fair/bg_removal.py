import cv2
import os
import time
import mediapipe as mp
import numpy as np

filepath = "/Users/coryfan/CS_Club/Project_2022/Club_Fair/Data/Frames/Video3/"
writepath = "/Users/coryfan/CS_Club/Project_2022/Club_Fair/Data/Completed/Video3/"

selfSeg = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)
filedir = os.listdir(filepath)

BG_COLOR = (192, 192, 192) # gray
MASK_COLOR = (255, 255, 255) # white

i = 0
for file in filedir:
    if (file == ".DS_Store"):
        continue
    print(file)
    image = cv2.imread(filepath+file)
    results = selfSeg.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.00001
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    res = np.where(condition, image, bg_image)
    cv2.imwrite(writepath+"im-"+str(i)+".jpg",res)
    i += 1
