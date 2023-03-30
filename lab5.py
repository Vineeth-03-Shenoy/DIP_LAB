import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\vinee\Desktop\3rd_YEAR\DIP\DigImgProc\Car.png', 0)
img = cv2.resize(image, (780,400))

# Perform histogram equalization to enhance contrast
img_eq = cv2.equalizeHist(img)

# Apply adaptive thresholding to segment the image
thresh = cv2.adaptiveThreshold(img_eq,
                               255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY,
                               11,
                               2
                                )

# Display the original, enhanced, and segmented images
cv2.imshow('Original', img)
cv2.imshow('Enhanced', img_eq)
cv2.imshow('Segmented', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()



