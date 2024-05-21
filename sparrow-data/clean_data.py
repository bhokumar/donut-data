import os
import shutil

def clean_directory(directory_path):
    """
    Remove all files and subdirectories in the specified directory.
    
    Parameters:
    directory_path (str): Path to the directory to clean.
    """
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove file or symbolic link
                print(f"Removed file: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove directory
                print(f"Removed directory: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.
    
    Parameters:
    directory_path (str): Path to the directory to create.
    """
    try:
        # Check if the directory already exists
        if not os.path.exists(directory_path):
            # Create the directory
            os.makedirs(directory_path)
            print(f"Directory created: {directory_path}")
        else:
            print(f"Directory already exists: {directory_path}")
    except Exception as e:
        print(f"Failed to create directory {directory_path}. Reason: {e}")

def main():
    original_directory = './docs/input/invoices/Dataset with valid information'
    clean_directory(original_directory)

    image_directory = './docs/input/invoices/processed/images'
    clean_directory(image_directory)

    ocr_directory = './docs/input/invoices/processed/ocr'
    clean_directory(ocr_directory)

    output_directory = './docs/input/invoices/processed/output'
    clean_directory(output_directory)

    test_directory = './docs/models/donut/data/img/test'
    clean_directory(test_directory)

    train_directory = './docs/models/donut/data/img/train'
    clean_directory(train_directory)

    validation_directory = './docs/models/donut/data/img/train'
    clean_directory(validation_directory)

    data_key_directory = './docs/models/donut/data/key'
    clean_directory(data_key_directory)

    sparraw_ui_json_directory = '../sparrow-ui/docs/json'
    clean_directory(sparraw_ui_json_directory)

    sparraw_ui_json_key_directory = '../sparrow-ui/docs/json/key'
    create_directory(sparraw_ui_json_key_directory)

    data_key_image_directory = '../docs/models/donut/data/key/img'
    create_directory(data_key_image_directory)

if __name__ == '__main__':
    main()