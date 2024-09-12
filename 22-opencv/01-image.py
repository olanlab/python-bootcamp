
import os
import cv2

dirname, filename  = os.path.split(os.path.abspath(__file__))

# Load an image from file
image = cv2.imread(f'{dirname}/image.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press indefinitely or for a specified amount of time in milliseconds
    cv2.waitKey(0)  # 0 means wait indefinitely

    # Save a copy of the image
    cv2.imwrite('image_copy.jpg', image)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
