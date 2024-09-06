import argparse
import os
import json

class MetaManager:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)

    def list_meta_info(self):
        datasets = os.listdir(self.dataset_dir)
        if datasets:
            print("Available datasets:")
            for dataset in datasets:
                print(f"- {dataset}")
        else:
            print("No datasets available.")

    def print_meta_info(self, dataset_name):
        dataset_path = os.path.join(self.dataset_dir, dataset_name, 'metadata.json')
        if os.path.exists(dataset_path):
            with open(dataset_path, 'r') as f:
                metadata = json.load(f)
                print(f"Metadata for {dataset_name}:")
                print(json.dumps(metadata, indent=4))
        else:
            print(f"Metadata for dataset {dataset_name} not found.")

    def add_meta_info(self, dataset_name):
        dataset_path = os.path.join(self.dataset_dir, dataset_name)
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
            metadata_path = os.path.join(dataset_path, "metadata.json")
            metadata = {"name": dataset_name, "description": "", "version": "1.0"}
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=4)
            print(f"Dataset {dataset_name} created with default metadata.")
        else:
            print(f"Dataset {dataset_name} already exists.")
    def license(self, dataset_name):
        license_path = os.path.join(self.dataset_dir, dataset_name, 'LICENSE')
        if os.path.exists(license_path):
            with open(license_path, 'r') as f:
                license_info = f.read()
                print(f"License for {dataset_name}:")
                print(license_info)
        else:
            print(f"License file for dataset {dataset_name} not found.")

def print_usage():
    usage_text = """
Usage of manage_meta.py:
    python manage_meta.py --list                    List all available datasets
    python manage_meta.py --load dataset_name       Print metadata of a specific dataset by name
    python manage_meta.py --add dataset_name        Add a new dataset with default metadata
    python manage_meta.py --license dataset_name     Print license information about a specific dataset

Example Usages:
    - List all datasets:
        python manage_meta.py --list
    - Load metadata for a dataset named 'my_dataset':
        python manage_meta.py --about my_dataset
    - Add a new dataset called 'new_dataset':
        python manage_meta.py --add new_dataset
    - print license information about a dataset called 'new_dataset':
        python manage_meta.py --license new_dataset
    """
    print(usage_text)

def main():
    parser = argparse.ArgumentParser(description="Dataset Metadata Manager", add_help=False)
    parser.add_argument("--list", action="store_true", help="List all datasets")
    parser.add_argument("--about", type=str, help="Load metadata for a specific dataset")
    parser.add_argument("--add", type=str, help="Add a new dataset with default metadata")
    parser.add_argument("--license", type=str, help="Print License information about the dataset")

    args = parser.parse_args()

    manager = MetaManager(dataset_dir="dataset_meta")

    if args.list:
        manager.list_meta_info()
    elif args.about:
        manager.print_meta_info(args.about)
    elif args.add:
        manager.add_meta_info(args.add)
    elif args.license:
        manager.license(args.license)
    else:
        print_usage()

if __name__ == "__main__":
    main()
