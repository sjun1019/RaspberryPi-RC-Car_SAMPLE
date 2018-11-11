### BY LSJ with SAMPLE
### 2018.10.28 //ui edit
### raspberry pi car project
### part of camera viewer

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 550)
cap.set(cv2.CAP_PROP_FPS, 60)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()