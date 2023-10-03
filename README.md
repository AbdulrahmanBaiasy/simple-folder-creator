# simple-folder-creator

The function called create_folders() creates a folder structure with subfolders. The function takes four arguments:

parent_folder: The name of the parent folder.
folder_names: A list of the names of the folders to create.
num_subfolders: The number of subfolders to create per folder.
subfolder_names: A list of the names of the subfolders to create.
The function works by iterating over the folder_names list and creating a folder for each name. It then replaces any spaces in the folder names with underscores. For each folder, the function creates a number of subfolders equal to the value of the num_subfolders argument. It then iterates over the subfolder_names list and creates a subfolder for each name.

The main function of the code prompts the user to enter the name of the parent folder, the number of folders to create, and the number of subfolders per folder. It then creates a list of folder names and a list of subfolder names based on the user input. It then calls the create_folders() function to create the folder structure. Finally, it prints a message to the user indicating that the folder structure has been created.
