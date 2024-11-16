import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    exit()

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
output_path = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(output_path, fourcc, 20, (width, height))

normal_speed = 50
slow_speed = 10
fast_speed = 1000
current_speed = normal_speed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)
    output.write(frame)
    k = cv2.waitKey(current_speed)

    if k == ord("q"):
        break
    elif k == ord("s"):
        current_speed = slow_speed
    elif k == ord("f"):
        current_speed = fast_speed
    elif k == ord("n"):
        current_speed = normal_speed

cap.release()
output.release()
cv2.destroyAllWindows()
