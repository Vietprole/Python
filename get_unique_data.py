import os
import shutil
from collections import defaultdict

def get_unique_data(folder_path, save_path, data_usage):
    folder_path = folder_path + data_usage + "/labels"
    image_path = folder_path.replace("labels", "images")
    save_path = save_path + data_usage + "/labels"
    image_save_path = save_path.replace("labels", "images")
    count = 0
    counts = defaultdict(int)
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        first_four_letters = filename[:4]

        # Increment the count for these first four letters
        counts[first_four_letters] += 1

        # If this is the first occurrence of these four letters, copy the file
        if counts[first_four_letters] == 1:
            shutil.copy(file_path, save_path + "/" + filename)  # Copy the label file
            if os.path.isfile(image_path + "/" + filename.replace("txt", "jpg")):
                shutil.copy(image_path + "/" + filename.replace("txt", "jpg"), image_save_path + "/" + filename.replace("txt", "jpg"))  # Copy the image file
            else:
                shutil.copy(image_path + "/" + filename.replace("txt", "jpeg"), image_save_path + "/" + filename.replace("txt", "jpeg"))

    print("Total unique chicken images: ", len(counts))
    return count

folder_path = "E:/Downloads/mickey finder.v1i.yolov8"
save_path = "E:/Downloads/mickey finder.v1i.yolov8/unique"
data_usage = "/valid"

get_unique_data(folder_path, save_path, data_usage)