import os
import cv2

dirname, filename  = os.path.split(os.path.abspath(__file__))

# Load an image
image = cv2.imread(f'{dirname}/people.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
