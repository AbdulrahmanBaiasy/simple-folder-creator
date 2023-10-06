# Folder Structure Creator

This Python script allows you to easily create a folder structure with subfolders. It provides a user-friendly interface for entering folder names, the number of parent folders to create, and the number of subfolders per parent folder.

## How to Use

1. Run the script in your Python environment.

2. You will be prompted to enter the following information:
   - Name of the parent folder where the structure will be created.
   - Number of parent folders to create.
   - Names of the parent folders.
   - Number of subfolders to create per parent folder.
   - Names of the subfolders.

3. The script will then create the specified folder structure in the provided parent folder. It will replace spaces in folder names with underscores.

4. After the process is complete, you will see a message indicating that the folder structure has been successfully created.

## Function Descriptions

- `sanitize_folder_name(name)`: This function replaces spaces with underscores in folder names.

- `create_subfolders(parent_folder, subfolder_names)`: This function creates subfolders for a given parent folder.

- `create_folders(parent_folder, parent_folder_names, num_subfolders_per_folder, subfolder_names)`: This function creates parent folders and their subfolders based on user input.

- `main()`: The main function handles user input and execution of the folder structure creation process.

## Example

Here's an example of how to use the script:

1. Enter the name of the parent folder: `My_Project`
2. Enter the number of parent folders to create: `2`
3. Enter a name for Parent Folder 1: `Documents`
4. Enter a name for Parent Folder 2: `Images`
5. Enter the number of subfolders per folder: `3`
6. Enter a name for Subfolder 1: `Drafts`
7. Enter a name for Subfolder 2: `Photos`
8. Enter a name for Subfolder 3: `Designs`

The script will create the following structure:

My_Project
│
├── Documents
│ ├── Drafts
│ ├── Photos
│ ├── Designs
│
└── Images
├── Drafts
├── Photos
├── Designs


## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

## Authors
- [Abdulrahman Baiasy](https://github.com/AbdulrahmanBaiasy)
- [Somar Kesen](https://github.com/somarkn99)

<br>

Enjoy creating organized folder structures with ease!

