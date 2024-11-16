import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
img = cv2.imread(r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg", cv2.IMREAD_COLOR)
if img is None:
    print("Error: Could not read the image. Please check the file path.")
else:
    img = cv2.resize(img, (600, 600))
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
