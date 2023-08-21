import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load image using PIL

image = Image.open('image.png')

# Convert image to NumPy array
image_array = np.array(image)

# Display the original image
plt.figure(figsize=(8, 6))
plt.imshow(image_array)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Convert the image to grayscale
gray_image = np.mean(image_array, axis=2).astype(np.uint8)

# Display the grayscale image
plt.figure(figsize=(8, 6))
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Apply a Gaussian blur to the image
from scipy.ndimage import gaussian_filter

blurred_image = gaussian_filter(gray_image, sigma=3)

# Display the blurred image
plt.figure(figsize=(8, 6))
plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')
plt.show()
