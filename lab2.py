import cv2
import numpy as np

# Load the image
image = cv2.imread(r'/home/vineeth/Documents/directory_env/digImgProcEnv/DIP_LAB/NOODLES.webp')
img = cv2.resize(image, (780,500))

# Define the rotation angle, scale factor, and translation
angle = 45
scale = 1.5
tx = 50
ty = 100

# Compute the rotation matrix using the rotation angle
center = (img.shape[1] // 2, img.shape[0] // 2)
M_rotate = cv2.getRotationMatrix2D(center, angle, scale)

# Compute the translation matrix
M_translate = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the rotation and translation
image_rotated = cv2.warpAffine(img, M_rotate, (img.shape[1], img.shape[0]))
image_transformed = cv2.warpAffine(img, M_translate, (img.shape[1], img.shape[0]))
image_combined = cv2.warpAffine(image_rotated, M_translate, (img.shape[1], img.shape[0]))

# Display the original image and the transformed image
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', image_rotated)
cv2.imshow('Transformed Image', image_transformed)
cv2.imshow('Combines Image',image_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()