import os
import cv2

dirname, filename  = os.path.split(os.path.abspath(__file__))

# Load an image from file
image = cv2.imread(f'{dirname}/image.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
