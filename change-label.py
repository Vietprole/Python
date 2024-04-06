import os
import cv2

folder_path = 'E:/OneDrive - The University of Technology/chicken_image/kaggle-antoreepjana-animals-detection-images-dataset-1050/train-388/labels'  # Replace with the actual path to your folder
image_path = 'E:/OneDrive - The University of Technology/chicken_image/kaggle-antoreepjana-animals-detection-images-dataset-1050/train-388'
# https://github.com/ultralytics/yolov5/discussions/7932
# find center: x = ((x2 - x1) / 2) + x1, y = ((y2 - y1) / 2) + y1
# find ratio of x,y to width, height: x = x / width, y = y / height
# find ratio of box to width, height: box_width = (x2 - x1) / width, box_height = (y2 - y1) / height


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

            # Get the base name without extension
            base_name = os.path.splitext(filename)[0]

            # Add the new extension
            new_filename = base_name + '.jpg'

            # Get the new file path
            new_file_path = os.path.join(image_path, new_filename)

            # Load an image
            img = cv2.imread(new_file_path)
            # Get the height and width of the image
            height, width = img.shape[:2]
            new_columns = columns.copy()

            for index, column in enumerate(columns):
                if index == 0:
                    new_columns[index] = '0'  # Change the first column to "0"
                elif index % 4 == 1:
                    x = (float(columns[index+2]) - float(columns[index]))/2 + float(columns[index]) 
                    new_columns[index] = str(x / width)
                elif index % 4 == 2:
                    y = (float(columns[index+2]) - float(columns[index]))/2 + float(columns[index]) 
                    new_columns[index] = str(y / height)
                elif index % 4 == 3:
                    x = float(columns[index]) - float(columns[index-2])
                    new_columns[index] = str(x / width)
                else:
                    y = float(columns[index]) - float(columns[index-2])
                    new_columns[index] = str(y / height)

            modified_line = ' '.join(new_columns)
            modified_lines.append(modified_line)
        
        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)