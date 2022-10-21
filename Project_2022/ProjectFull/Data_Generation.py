import cv2

video = cv2.VideoCapture("./Data-Videos/JonOct21.mp4")

success = True

count=0
period = 7

while success:
    success, image = video.read()
    if success and count%period != 0:
        cv2.imwrite("./Frames/JonOct21/Image%d.jpg" % (count/period), image)
        print("Read frame:", count)
    count+=1

print("DONE")
