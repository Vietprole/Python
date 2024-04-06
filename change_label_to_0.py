import os
import cv2

folder_path = "E:/OneDrive - The University of Technology/chicken_image/kaggle-ksvbist-chicken-1573/labels - Copy/val"  # Replace with the actual path to your folder

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Modify the contents of the file
        modified_lines = []

        for line in lines:
            columns = line.split()
            columns[0] = '0'  # Change the first column to "0"
            modified_lines.append(' '.join(columns))  # Join the columns with a space

        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.writelines('\n'.join(modified_lines))