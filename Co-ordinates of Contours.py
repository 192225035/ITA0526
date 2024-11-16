import cv2
import numpy as np

def find_contours(image_path):
    """
    Finds contours in an image and returns their coordinates.

    Parameters:
    - image_path: str, path to the input image.

    Returns:
    - contours: list of numpy arrays, each containing the coordinates of a contour.
    - hierarchy: numpy array, the hierarchy of the contours.
    """
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return None, None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding or edge detection
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # Alternatively, you can use Canny edge detection
    # binary = cv2.Canny(gray, 100, 200)

    # Find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours, hierarchy

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg"
    contours, hierarchy = find_contours(image_path)

    # Print the coordinates of the contours
    if contours is not None:
        for i, contour in enumerate(contours):
            print(f"Contour {i}: {contour}")
