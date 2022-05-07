import cv2
import numpy as np
import hand as htm
import time
from pynput.mouse import Button, Controller
import math

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
detect = htm.handDetector(maxHands=1)
while True:
    ret, img = cap.read()
    img = cv2.resize(img, (0, 0), fx=1.8, fy=1.4)
    img = detect.findHands(img)
    lmlist, bb = detect.findPosition(img)
    if len(lmlist)!=0:
        x1,y1 = lmlist[8][1:]
        xclick,yclick = lmlist[7][1:]
        xscroll,yscroll = lmlist[4][1:]
        xscroll2,yscroll2 = lmlist[3][1:]

        x2,y2 = lmlist[12][1:]
        fin = detect.fingersUp()
        #print(fin)

        mouse = Controller()
        mouse.position = (width*2.0-x2,y2*1.8)
        if (math.sqrt(math.pow((x1-xclick),2)+math.pow((y1-yclick),2))) < 25:
            # cv2.circle(img,(x1,x2),5,(255,0,0),3)
            # print(math.sqrt(math.pow((x1-xclick),2)+math.pow((y1-yclick),2)))
            mouse.click(Button.left,1)
        if (math.sqrt(math.pow((x1 - xscroll), 2) + math.pow((y1 - yscroll), 2))) < 50:
            print(math.sqrt(math.pow((x1 - xscroll), 2) + math.pow((y1 - yscroll), 2)))
            mouse.scroll(0, -1)
        if(xscroll<xscroll2):
            mouse.scroll(0, 1)

    cv2.imshow("img",img)

    cv2.waitKey(1)
