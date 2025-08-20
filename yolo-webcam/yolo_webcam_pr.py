from ultralytics import YOLO
import cvzone as cz
import cv2 as c
# import numpy as np
import math as m

cap=c.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

model = YOLO("../yolo-weights/yolov8n.pt")
while True:
    scs, img = cap.read()
    # c.imshow('img',img)
    rb = model(img,stream=True)
    for i in rb:
        box=i.boxes
        for bx in box:
            x1,y1,x2,y2=map(int,bx.xyxy[0])
            print(x1,y1,x2,y2)
            # c.rectangle(img,(x1,y1),(x2,y2),(255,150,255),3) 
            w, h = x2-x1, y2-y1
            cz.cornerRect(img,(x1,y1,w,h))
            con = m.ceil((bx.conf[0]*100)/100)
            print(con)
            cz.putTextRect(img,f"{con}%",(max(0,x1),max(50,y1)))

    c.imshow('img',img)
    c.waitKey(1)


