import os

def create_folders(parent_folder, folder_names, num_subfolders, subfolder_names):
    for folder_name in folder_names:
        # Replace spaces with underscores in folder names
        folder_name = folder_name.replace(" ", "_")
        
        folder_path = os.path.join(parent_folder, folder_name)
        os.makedirs(folder_path)

        for subfolder_name in subfolder_names:
            subfolder_path = os.path.join(folder_path, subfolder_name)
            os.makedirs(subfolder_path)

def main():
    parent_folder = input("Enter the name of the parent folder: ")
    num_folders = int(input("Enter the number of folders to create: "))
    
    folder_names = []
    for i in range(1, num_folders + 1):
        folder_name = input(f"Enter a name for Folder {i}: ")
        folder_names.append(folder_name)

    num_subfolders = int(input("Enter the number of subfolders per folder: "))
    
    subfolder_names = []
    for i in range(1, num_subfolders + 1):
        subfolder_name = input(f"Enter a name for Subfolder {i}: ")
        subfolder_names.append(subfolder_name)

    create_folders(parent_folder, folder_names, num_subfolders, subfolder_names)
    print(f"Folder structure created in '{parent_folder}'.")

if __name__ == "__main__":
    main()
