import cv2
import numpy as np

# Define the kernel for morphological operations (if needed)
kernel = np.ones((5, 5), np.uint8)

# Read the image from the specified path
img = cv2.imread(r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
    exit()

# Resize the image
img = cv2.resize(img, (1, 60))

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
