import os

def organize_files(directory, mapping):
    # Ensure directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist!")
        return
    
    # Process each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            
            # Get the folder name from mapping, default to 'Others' if not found
            folder_name = mapping.get(file_extension, 'Others')
            folder_path = os.path.join(directory, folder_name)
            
            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Move file to respective folder
            os.rename(file_path, os.path.join(folder_path, filename))
    
    print("Files have been organized!")

def main():
    print("Welcome to the File Organizer!")
    
    # 3. Getting User Input
    directory = input("Please enter the path to the directory you want to organize: ")
    
    # 4. Mapping Extensions to Folder Names
    mapping = {
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.png': 'Images',
        # Add more mappings as needed
    }
    
    # Process the directory
    organize_files(directory, mapping)

main()
