import kagglehub
import shutil
import os

current_location = os.getcwd()
datasets_location = r'C:\Users\nijaa\.cache\kagglehub\datasets'

def load_dataset(location):
    # Download latest version
    path = kagglehub.dataset_download(location)
    print("Path to dataset files:", path)

    # Walk through all files and directories in the dataset
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            source_file = os.path.join(root, filename)

            # Create the same folder structure in the destination
            relative_path = os.path.relpath(root, path)
            destination_folder = os.path.join(current_location, relative_path)
            os.makedirs(destination_folder, exist_ok=True)

            # Copy the file to the destination
            # destination_file = os.path.join(destination_folder, filename)
            shutil.copy(source_file, current_location)
            print(f"Copied: {filename} to {current_location}")


if __name__ == '__main__':
    dataset_location = input("Enter the Kaggle dataset identifier or path: ")
    load_dataset(dataset_location)