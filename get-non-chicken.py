import os
import shutil

def get_sick_chicken(folder_path, save_path, data_usage):
    folder_path = folder_path + data_usage + "/labels"
    image_path = folder_path.replace("labels", "images")
    save_path = save_path + data_usage + "/labels"
    image_save_path = save_path.replace("labels", "images")
    count = 0
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    columns = line.split()
                    if columns[0] != '0':
                        shutil.copy(file_path, save_path + "/" + filename)  # Copy the label file
                        if os.path.isfile(image_path + "/" + filename.replace("txt", "jpg")):
                            shutil.copy(image_path + "/" + filename.replace("txt", "jpg"), image_save_path + "/" + filename.replace("txt", "jpg"))  # Copy the image file
                        else:
                            shutil.copy(image_path + "/" + filename.replace("txt", "jpeg"), image_save_path + "/" + filename.replace("txt", "jpeg"))
                        count += 1
                        break

    print("Total sick chicken images: ", count)
    return count

folder_path = "E:/Downloads/Chicken Combs.v3i.yolov7pytorch"
save_path = "E:/Downloads/Chicken Combs.v3i.yolov7pytorch/sick-chicken"
data_usage = "/train"

get_sick_chicken(folder_path, save_path, data_usage)