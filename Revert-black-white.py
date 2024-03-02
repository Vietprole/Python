from PIL import Image
import numpy as np

# Open the image file
img = Image.open('C:/Users/OS/Downloads/simple-chicken-icon-illustration-design-260nw-2321927785.webp').convert('L')

# Convert the image to a numpy array
img_array = np.array(img)

# Invert colors (black becomes white and white becomes black)
img_inverted_array = 255 - img_array

# Convert the numpy array back to an image
img_inverted = Image.fromarray(img_inverted_array)

# Save the new image
img_inverted.save('my_image_black_and_white.png')