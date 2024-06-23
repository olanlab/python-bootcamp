import os
import cv2

dirname, filename  = os.path.split(os.path.abspath(__file__))

# Load an image from file
image = cv2.imread(f'{dirname}/image.png')

# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a circle
cv2.circle(image, (300, 300), 100, (255, 0, 0), -1)

# Display the image with shapes
cv2.imshow('Image with Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
