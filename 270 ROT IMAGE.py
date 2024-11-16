import cv2
img = cv2.imread(r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg")
if img is None:
    print("Error: Could not read the image.")
    exit()
rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image (270 degrees)", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
