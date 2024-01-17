import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image from file
image_path = 'images/Publishing.jpg'
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display the original and processed images
plt.subplot(131), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(gray_image, cmap='gray'), plt.title('Grayscale Image')
plt.subplot(133), plt.imshow(blurred_image, cmap='gray'), plt.title('Blurred Image')
plt.show()