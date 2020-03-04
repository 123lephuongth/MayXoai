import cv2 as cv
import numpy as np
from Source.Kich_Thuoc_Thu_Tu import *

cap = cv.VideoCapture('Xoai4.mp4')
tam = 0
so = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    cv.line(frame, (0, 70), (952, 70), (255, 0, 0), 2)
    cv.line(frame, (0, 150), (952, 150), (255, 0, 0), 2)
    cv.line(frame, (0, 210), (952, 210), (255, 0, 0), 2)
    cv.line(frame, (475, 0), (475, 712), (255, 0, 0), 2)
    cv.line(frame, (910, 0), (910, 712), (255, 0, 0), 2)
    Tong = [tam,so,frame]
    kich_thuoc_qua = tong(Tong)
    cv.imshow('a',kich_thuoc_qua)

    if cv.waitKey(15) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()