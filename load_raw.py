import os
import subprocess
import argparse

# Define dataset URLs
DATASET_URLS = {
    "imagenet": "http://www.image-net.org/download-image-net",  # Replace this with the actual ImageNet URL
    "cifar10": "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz",
    "mnist": "http://yann.lecun.com/exdb/mnist/"
}


class RawDataLoader:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)

    def download_dataset(self, dataset_name):
        dataset_url = DATASET_URLS.get(dataset_name)
        if not dataset_url:
            print(f"Dataset '{dataset_name}' is not recognized. Available datasets are: {list(DATASET_URLS.keys())}")
            return

        dataset_path = os.path.join(self.dataset_dir, dataset_name)
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

        print(f"Downloading dataset: {dataset_name}")
        try:
            # Use wget to download the dataset
            subprocess.run(f"wget -P {dataset_path} {dataset_url}", shell=True, check=True)
            print(f"Dataset '{dataset_name}' downloaded successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to download dataset from {dataset_url}")

    def extract_dataset(self, dataset_name):
        dataset_path = os.path.join(self.dataset_dir, dataset_name)

        # Find any zip/tar.gz files and extract them
        for file in os.listdir(dataset_path):
            file_path = os.path.join(dataset_path, file)
            if file.endswith(".zip"):
                print(f"Extracting {file}...")
                subprocess.run(f"unzip -d {dataset_path} {file_path}", shell=True)
            elif file.endswith(".tar.gz"):
                print(f"Extracting {file}...")
                subprocess.run(f"tar -xzf {file_path} -C {dataset_path}", shell=True)

        print(f"Extraction completed for {dataset_name}.")


def print_usage():
    usage_text = """
Usage of load_raw.py:
    python load_raw.py dataset_name         Download and extract the specified raw dataset

Available datasets:
    - imagenet
    - cifar10
    - mnist

Example Usages:
    - Download and extract the ImageNet dataset:
        python load_raw.py imagenet
    - Download and extract the CIFAR-10 dataset:
        python load_raw.py cifar10
    """
    print(usage_text)


def main():
    parser = argparse.ArgumentParser(description="Raw Dataset Loader")
    parser.add_argument("dataset", type=str,
                        help="The name of the dataset to download (e.g., imagenet, cifar10, mnist)")

    args = parser.parse_args()

    loader = RawDataLoader(dataset_dir="raw_data")

    # Download the dataset from the provided name
    loader.download_dataset(args.dataset)

    # Extract the dataset
    loader.extract_dataset(args.dataset)


if __name__ == "__main__":
    main()
