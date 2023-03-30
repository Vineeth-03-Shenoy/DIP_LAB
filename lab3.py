import cv2
import numpy as np

# read the image
image = cv2.imread(r'C:\Users\vinee\Desktop\3rd_YEAR\DIP\DigImgProc\Car.png', 0)
img = cv2.resize(image, (780,500))

# define the kernel for erosion and dilation
kernel = np.ones((5,5), np.uint8)

# apply erosion to the image
erosion = cv2.erode(img, kernel, iterations=1)

# apply dilation to the image
dilation = cv2.dilate(img, kernel, iterations=1)

# subtract the erosion result from the original image
erosion_edge = cv2.absdiff(img, erosion)

# subtract the dilation result from the original image
dilation_edge = cv2.absdiff(img, dilation)

# display the original image and erosion edge image
cv2.imshow("Original Image", img)
cv2.imshow("Erosion Image", erosion)
cv2.imshow("Erosion Edge Image", erosion_edge)

# display the original image and dilation edge image
cv2.imshow("Dilation Image", dilation)
cv2.imshow("Dilation Edge Image", dilation_edge)

# wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()