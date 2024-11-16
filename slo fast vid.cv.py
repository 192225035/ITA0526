import cv2
import numpy as np
path=r"C:\Users\GOUSE\OneDrive\Desktop\opencvApp\fast clip.mp4"
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print("Error opening video file")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(250) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()
