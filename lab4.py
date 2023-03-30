import cv2
import numpy as np

# read the image
image = cv2.imread(r'C:\Users\vinee\Desktop\3rd_YEAR\DIP\DigImgProc\Car.png', 0)
img = cv2.resize(image, (780,400))

# define the kernels for filtering
sobel_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
gaussian_kernel = cv2.getGaussianKernel(10, 0)

# apply the filters to the image
sobel_edges = cv2.filter2D(img, -1, sobel_kernel)
laplacian_edges = cv2.filter2D(img, -1, laplacian_kernel)
gaussian_texture = cv2.filter2D(img, -1, gaussian_kernel)

# display the original image and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edges', sobel_edges)
cv2.imshow('Laplacian Edges', laplacian_edges)
cv2.imshow('Gaussian Texture', gaussian_texture)

# wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()