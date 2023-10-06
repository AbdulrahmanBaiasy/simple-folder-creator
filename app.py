import os

# Function to sanitize folder names (replace spaces with underscores)
def sanitize_folder_name(name):
    return name.replace(" ", "_")

# Function to create subfolders for a given parent folder
def create_subfolders(parent_folder, subfolder_names):
    for subfolder_name in subfolder_names:
        subfolder_path = os.path.join(parent_folder, subfolder_name)
        os.makedirs(subfolder_path)

# Function to create parent folders and their subfolders
def create_folders(parent_folder, parent_folder_names, num_subfolders_per_folder, subfolder_names):
    for folder_name in parent_folder_names:
        sanitized_folder_name = sanitize_folder_name(folder_name)
        folder_path = os.path.join(parent_folder, sanitized_folder_name)
        os.makedirs(folder_path)
        
        # Create subfolders for each parent folder
        create_subfolders(folder_path, subfolder_names * num_subfolders_per_folder)

# Main function for user input and execution
def main():
    parent_folder = input("Enter the name of the parent folder: ")
    num_parent_folders = int(input("Enter the number of parent folders to create: "))
    
    parent_folder_names = []
    for i in range(1, num_parent_folders + 1):
        folder_name = input(f"Enter a name for Parent Folder {i}: ")
        parent_folder_names.append(folder_name)

    num_subfolders_per_folder = int(input("Enter the number of subfolders per folder: "))
    
    subfolder_names = []
    for i in range(1, num_subfolders_per_folder + 1):
        subfolder_name = input(f"Enter a name for Subfolder {i}: ")
        subfolder_names.append(subfolder_name)

    # Create the folder structure
    create_folders(parent_folder, parent_folder_names, num_subfolders_per_folder, subfolder_names)
    
    print(f"Folder structure created in '{parent_folder}'.")

if __name__ == "__main__":
    main()
