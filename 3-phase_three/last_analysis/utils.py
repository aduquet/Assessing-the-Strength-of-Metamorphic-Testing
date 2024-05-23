import os
import shutil


class Utils():
    
    def copy_file_to_directories(source, destination):
        shutil.copy2(source, destination)
    
    def copy_direct_to_directories(source_directory, destination_directory):
        # Remove the destination directory if it exists
        if os.path.exists(destination_directory):
            shutil.rmtree(destination_directory)

        # Copy the entire directory tree from source to destination
        shutil.copytree(source_directory, destination_directory)
        
    def replace_string_in_file(file_path, search_string, replace_string):
        # Check if the file exists
        if not os.path.isfile(file_path):
            return "File does not exist."
        
    # Function to create directories based on file names
    def create_directories(folder_name, base_directory):
        
        # folder_name = os.path.join(base_directory, file_name)
        # Create the full path for the new folder
        new_folder_path = os.path.join(base_directory, folder_name)
        # print(new_folder_path)
        # Create the folder if it doesn't exist
        os.makedirs(new_folder_path, exist_ok=True)
        
        return new_folder_path
    
    def get_name(file_path):
        return os.path.splitext(file_path.split('/')[-1])[0]