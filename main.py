import os
import shutil

desktop_path = f"/Users/username/Desktop"  # Replace with your Mac username
destination_folder = "/Users/username/Documents/Dedicated_Folder"  # Replace with desired folder

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_files_to_destination(file_path, destination_path):
    create_folder_if_not_exists(destination_path)
    shutil.move(file_path, destination_path)

def main():
    files_on_desktop = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    for file_name in files_on_desktop:
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension:
            category_folder = os.path.join(destination_folder, file_extension[1:])
            source_file_path = os.path.join(desktop_path, file_name)
            move_files_to_destination(source_file_path, category_folder)
            print(f"Moved {file_name} to {category_folder}")

if __name__ == "__main__":
    main()
