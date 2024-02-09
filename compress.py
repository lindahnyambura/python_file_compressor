#!/usr/bin/python3

import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    """
    Compress a folder using the specified compression type
    
    Args:
        folder_path (str): Path of the folder to compress
        compress_type (str): Type of compression to use (zip, tar, tgz)
    
    Returns:
        None
    """
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_filename = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

        elif compress_type == "tar":
            with tarfile.open(compressed_filename, "w") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            with tarfile.open(compressed_filename, "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        
        print(f"Folder compressed successfully: {compressed_filename}")
    except Exception as e:
        print(f"Error compressing folder: {str(e)}")

def main():
    """
    Main function to compress a folder
    """
    folder_path = input("Enter the folder path: ")

    if not os.path.exists(folder_path):
        print("Folder not found")
        return
    
    compress_types = ["zip", "tar", "tgz"]
    print("Available compression types:")
    for i, comp_type in enumerate(compress_types, 1):
        print(f"{i}. {comp_type}")

    choice = int(input("Enter your choice: "))
    if 1 <= choice <= len(compress_types):
        compress_type = compress_types[choice-1]
        compress_folder(folder_path, compress_type)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
