# Motion Dataset Manager

This is a manager designed to manage motion datasets through the command line. The manager allows you to list, load, and add motion datasets.

## Features

- **List Datasets**: View all datasets available in the dataset directory.
- **Load Dataset**: Load and process a specific dataset by name.
- **Add Dataset**: Create a new dataset folder with a given name.

## Current Structure

The script expects a directory named `dataset_meta` in the same folder as `manage.py`. Inside this directory, each dataset meta descriptions is stored as a subfolder. 

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
