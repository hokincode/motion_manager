# Motion Dataset Manager

This is a manager designed to manage motion datasets through the command line. The manager allows you to list, load, and add motion datasets.

## Features

- **List Datasets**: View all datasets available in the dataset directory.
- **Load Dataset**: Load and process a specific dataset by name.
- **Add Dataset**: Create a new dataset folder with a given name.

## Current Structure

The `manager_directory/` structure is designed for managing raw and processed datasets along with their metadata. The `manage_meta.py` script handles operations related to dataset metadata, stored in the `dataset_meta/` directory, where each dataset has its own subfolder containing a `metadata.json` file and a `LICENSE` file. The `load_raw.py` script is responsible for fetching and organizing raw datasets, which are stored in the `raw_data/` directory. After raw data is processed by the `process_raw.py` script, the cleaned and formatted datasets are saved in the `processed_datasets/` directory, with each dataset in its respective subfolder. This structure ensures a clear separation between raw and processed data while keeping metadata well-organized, making it efficient for managing and processing datasets.

```
manager_directory/
│
├── manage_meta.py
├── dataset_meta/
│   ├── dataset_name_1/
│   │   ├── metadata.json
│   │   └── LICENSE
│   ├── dataset_name_2/
│   │   ├── metadata.json
│   │   └── LICENSE
│  └── ...  # Additional datasets' metadata
│
├── load_raw.py
├── raw_data/
    ├── raw_data_1
    ├── raw_data_1
    └── ...  # Additional raw datasets' files fetched from internet
│
├── process_raw.py
└── processed_datasets/
    ├── dataset_name_1/  # Dataset files (e.g., CSV, images, etc.)
    ├── dataset_name_2/  # Dataset files (e.g., CSV, images, etc.)
    └── ...  # Additional datasets' files
```
