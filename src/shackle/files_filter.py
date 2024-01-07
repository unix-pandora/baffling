import os


def find_files(directory_path, file_types):
    result = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.endswith(ft) for ft in file_types):
                result.append(os.path.join(root, file))
    return result
