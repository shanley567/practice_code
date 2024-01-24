import os

def find_and_replace_files(start_path, prefix, old_value, new_value):
    for foldername, subfolders, filenames in os.walk(start_path):
        for filename in filenames:
            if filename.startswith(prefix):
                file_path = os.path.join(foldername, filename)
                replace_in_file(file_path, old_value, new_value)

def replace_in_file(file_path, old_value, new_value):
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    new_content = file_content.replace(old_value, new_value)
    
    with open(file_path, 'w') as file:
        file.write(new_content)

# Example usage:
start_path = r"C:\Users\js105\Documents\Scripts"
file_prefix = "dasd"
old_str_value = "value 1"
new_str_value = "value 2"

find_and_replace_files(start_path, file_prefix, old_str_value, new_str_value)
