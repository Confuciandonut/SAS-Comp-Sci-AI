#Splits videos into individual images.

import cv2

video = cv2.VideoCapture("../ProjectFull/Data-Videos/CoryOct28.mov")

success = True

count=0
period = 3 #Frames per extracted image

while success:
    success, image = video.read()
    if success and count%period != 0:
        cv2.imwrite("/Users/coryfan/CS_Club/Project_2022/ProjectFull/Frames/CoryOct28/Image%d.png" % (count/period), image)
        print("Read frame:", count)
    count+=1

print("DONE")
