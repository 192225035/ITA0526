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

# Rotate the image by 180 degrees
rotated_img = cv2.rotate(img, cv2.ROTATE_90)

# Display the original and rotated images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image (180 degrees)", rotated_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
