import numpy as np
import cv2

data = cv2.VideoCapture('./sample.mp4')
type(data)
data.isOpened()
cascade = cv2.CascadeClassifier('cascade.xml')
while True:
    ret, frame = data.read()
    if ret:

        objects = cascade.detectMultiScale(frame, 1.1, 3)
        for (x, y, w, h) in objects:
            obj = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow(' sample data', obj)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)