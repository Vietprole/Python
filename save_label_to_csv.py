import csv
import os
import cv2

# folder_path = 'E:/OneDrive - The University of Technology/chicken_image/kaggle-antoreepjana-animals-detection-images-dataset-1050/train-388/labels'  # Replace with the actual path to your folder
# image_path = 'E:/OneDrive - The University of Technology/chicken_image/kaggle-antoreepjana-animals-detection-images-dataset-1050/train-388'
folder_path = "E:/Downloads/Chicken Combs.v3i.yolov7pytorch/train/labels"
image_path = "E:/Downloads/Chicken Combs.v3i.yolov7pytorch/train/images"
# https://github.com/ultralytics/yolov5/discussions/7932
# find center: x = (x2 - x1) / 2, y = (y2 - y1) / 2
# find ratio of x,y to width, height: x = x / width, y = y / height
# find ratio of box to width, height: box_width = (x2 - x1) / width, box_height = (y2 - y1) / height


# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Write the modified contents back to the file
        # Export data to CSV file
        # Write the contents to the CSV file
        with open('label.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            if file.tell() == 0:  # Write header only if file is empty
                writer.writerow(['Class', 'X_center', 'Y_center', 'Width', 'Height'])
            for line in lines:
                writer.writerow(line.split())