import os
import cv2

folder_path = 'E:/OneDrive - The University of Technology/chicken_image/kaggle-antoreepjana-animals-detection-images-dataset-1050/train-388/labels'  # Replace with the actual path to your folder

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
            new_columns = []

            # Append the first 5 columns to modified_lines
            first_five_columns = ' '.join(columns[:5])
            modified_lines.append(first_five_columns + '\n')

            for index in range(5, len(columns), 4):
                new_line = ['0']  # Start new line with "0"
                for i in range(4):
                    if index + i < len(columns):
                        new_line.append(columns[index + i])
                new_columns.append(' '.join(new_line))

            modified_lines.append('\n'.join(new_columns))

        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)