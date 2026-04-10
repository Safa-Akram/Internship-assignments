# Image as Numbers

import cv2

# Load image (keep image in same folder)
img = cv2.imread("sample.jpg")

# Print details
print("Shape (Height, Width, Channels):", img.shape)
print("Pixel value at (0,0):", img[0][0])
print("Total pixels:", img.size)
print("Number of channels:", img.shape[2])