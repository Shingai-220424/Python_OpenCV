import numpy as np
import cv2

data = cv2.VideoCapture('./sample.mp4')
type(data)
data.isOpened()
while True:
    ret, frame = data.read()
    if ret:
        cv2.imshow('sample data', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)