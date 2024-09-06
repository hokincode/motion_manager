import argparse
import os

class DatasetManager:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)

    def list_datasets(self):
        datasets = os.listdir(self.dataset_dir)
        if datasets:
            print("Available datasets:")
            for dataset in datasets:
                print(f"- {dataset}")
        else:
            print("No datasets available.")

    def load_dataset(self, dataset_name):
        dataset_path = os.path.join(self.dataset_dir, dataset_name)
        if os.path.exists(dataset_path):
            print(f"Loading dataset: {dataset_name}")
            # Add your code to load and process the dataset here
        else:
            print(f"Dataset {dataset_name} not found.")

    def add_dataset(self, dataset_name):
        dataset_path = os.path.join(self.dataset_dir, dataset_name)
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
            print(f"Dataset {dataset_name} created.")
        else:
            print(f"Dataset {dataset_name} already exists.")


def print_usage():
    usage_text = """
Usage of manage.py:
    python manage.py --list                 List all available datasets
    python manage.py --load dataset_name    Load a specific dataset by name
    python manage.py --add dataset_name     Add a new dataset with the given name

Example Usages:
    - List all datasets:
        python manage.py --list
    - Load a dataset named 'my_dataset':
        python manage.py --load my_dataset
    - Add a new dataset called 'new_dataset':
        python manage.py --add new_dataset
    """
    print(usage_text)


def main():
    parser = argparse.ArgumentParser(description="Dataset Manager", add_help=False)
    parser.add_argument("--list", action="store_true", help="List all datasets")
    parser.add_argument("--load", type=str, help="Load a specific dataset")
    parser.add_argument("--add", type=str, help="Add a new dataset")

    args = parser.parse_args()

    manager = DatasetManager(dataset_dir="datasets")

    if args.list:
        manager.list_datasets()
    elif args.load:
        manager.load_dataset(args.load)
    elif args.add:
        manager.add_dataset(args.add)
    else:
        print_usage()


if __name__ == "__main__":
    main()