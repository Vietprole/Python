import os
import shutil

folder_path = "E:/Downloads/OfficalDataset-fixed/OfficalDataset"

data_usages = ["/test", "/train", "/val"]
for data_usage in data_usages:
    folder_path = "E:/Downloads/OfficalDataset-fixed/OfficalDataset" + data_usage + "/labels"
    label_count = 0
    empty_count = 0
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                label_count += 1
            else:
                empty_count += 1
                print("Empty label: ", file_path)
    print("Total label in " + data_usage + ":", label_count)
    print("Empty label in " + data_usage + ":", empty_count)