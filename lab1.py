import cv2

# Load the image
img = cv2.imread(r"C:\Users\vinee\Desktop\3rd_YEAR\DIP\DigImgProc\NOODLES.webp")
image = cv2.resize(img, (780,500))

# Get the dimensions of the image
height, width, _ = image.shape

# Split the image into four quadrants
top_left = image[0:int(height/2), 0:int(width/2)]
top_right = image[0:int(height/2), int(width/2):width]
bottom_left = image[int(height/2):height, 0:int(width/2)]
bottom_right = image[int(height/2):height, int(width/2):width]

# Display the quadrants
cv2.imshow("ORIGINAL IMAGE", image)
cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

