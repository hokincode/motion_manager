# Motion Dataset Manager

This is a manager designed to manage motion datasets through the command line. The manager allows you to list, load, and add motion datasets.

## Features

- **List Datasets**: View all datasets available in the dataset directory.
- **Load Dataset**: Load and process a specific dataset by name.
- **Add Dataset**: Create a new dataset folder with a given name.

## Current Structure

The manager contains all the essential components for managing datasets and their metadata. The `manage.py` script provides a command-line interface to handle various dataset management tasks, such as loading, updating, and processing datasets. The `dataset_meta/` directory organizes metadata and licensing information for each dataset in individual subfolders, ensuring that each dataset's information is clearly separated and easy to access. The `datasets/` directory stores the actual dataset files in respective subdirectories, allowing for a clean and scalable structure that can accommodate multiple datasets. This layout promotes efficient data management and ensures clarity when dealing with large datasets and their corresponding metadata.
```
manager_directory/
│
├── manage.py
├── dataset_meta/
│   ├── dataset_name_1/
│   │   ├── metadata.json
│   │   └── LICENSE
│   ├── dataset_name_2/
│   │   ├── metadata.json
│   │   └── LICENSE
│   └── ...  # Additional datasets' metadata
│
└── datasets/
    ├── dataset_name_1/  # Dataset files (e.g., CSV, images, etc.)
    ├── dataset_name_2/  # Dataset files (e.g., CSV, images, etc.)
    └── ...  # Additional datasets' files
```
