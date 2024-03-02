# Importing Required Modules 
from rembg import remove 
from PIL import Image 

text = 'logo-pct.jpg'
# Store path of the image in the variable input_path 
input_path = "C:/Users/OS/Downloads/" + text

# Store path of the output image in the variable output_path 
output_path = "C:/Users/OS/Downloads/Background-removed/" + text

# Processing the image 
input = Image.open(input_path) 

text1 = 'logo-pct.png'
# Store path of the image in the variable input_path 
input_path1 = "C:/Users/OS/Downloads/" + text1
# Store path of the output image in the variable output_path 
output_path1 = "C:/Users/OS/Downloads/Background-removed/" + text1

# Save the image as a PNG
input.save(output_path1)

text1 = 'logo-pct.png'
# Store path of the image in the variable input_path 
input_path1 = "C:/Users/OS/Downloads/Background-removed/" + text1


# Processing the image 
input1 = Image.open(input_path1)

# Removing the background from the given Image 
output = remove(input1) 

# Convert the image to RGB mode
#rgb_img = output.convert('RGB')

#Saving the image in the given path 
output.save(output_path1) 
