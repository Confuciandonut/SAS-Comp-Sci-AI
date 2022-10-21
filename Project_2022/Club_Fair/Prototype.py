import cv2
import numpy as np
import torch

screen_width = 1440
screen_height = 900

print("LOADING MODEL")
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/coryfan/CS_Club/Project_2022/Club_Fair/Fair_Prototype.pt', force_reload=True)

img2 = None
frame = None
rval = False
hasframe = False
hasbox = False
threadActive = True
boxes = None
colors = {"C":(0,0,255),"S":(0,255,0)}
    
print("BEGINNING VIDEO")
cv2.namedWindow("Demo")
vc = cv2.VideoCapture(1)

while True:
    rval, frame = vc.read()
    frame_height, frame_width, _ = frame.shape
    key = cv2.waitKey(20)       
    frame = np.fliplr(frame)
    frame = cv2.resize(frame,(int(frame.shape[1]*0.5),int(frame.shape[0]*0.5)),interpolation = cv2.INTER_AREA)
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hasframe = True
    if (rval == False):
        break
    frame = frame.astype(np.uint8)
    boxes = model(img2).pandas().xyxy[0]
    print(boxes)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    for i in boxes.index:
        if (boxes['confidence'][i]>0.8):
            frame = cv2.rectangle(frame,(int(boxes['xmin'][i]),int(boxes['ymin'][i])),(int(boxes['xmax'][i]),int(boxes['ymax'][i])),colors[boxes['name'][i]],10)
    frame = cv2.resize(frame,(8000,4500))
    cv2.imshow("Demo", frame)

vc.release()
cv2.destroyWindow("Demo")
