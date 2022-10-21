import cv2

video = cv2.VideoCapture("/Users/coryfan/CS_Club/Project_2022/Club_Fair/Data/Videos/video13.mp4")

success = True

count=0
period = 10

while success:
    success, image = video.read()
    if success and count%period != 0:
        cv2.imwrite("/Users/coryfan/CS_Club/Project_2022/Club_Fair/Data/Frames/Video13/Image%d.jpg" % (count/period), image)
        print("Read frame:", count)
    count+=1

print("DONE")
