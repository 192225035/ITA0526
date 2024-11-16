import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread(r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
    exit()

# Get the dimensions of the image
(h, w) = img.shape[:2]

# Define the points for the affine transformation
# Original points (triangle in the original image)
points_original = np.float32([[50, 50], [200, 50], [50, 200]])

# New points (triangle in the transformed image)
points_transformed = np.float32([[10, 100], [200, 50], [100, 250]])

# Get the affine transformation matrix
affine_matrix = cv2.getAffineTransform(points_original, points_transformed)

# Perform the affine transformation
transformed_img = cv2.warpAffine(img, affine_matrix, (w, h))

# Display the original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", transformed_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
