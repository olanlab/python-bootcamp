import os
import cv2

dirname, filename  = os.path.split(os.path.abspath(__file__))

# Load an image
image = cv2.imread(f'{dirname}/image.png', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the result
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()