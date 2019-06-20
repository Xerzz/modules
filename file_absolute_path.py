import os


def file_abspath(file):
    location = os.path.realpath(os.path.dirname(__file__))
    path = os.path.join(location, file)
    return path

# script_path = os.path.abspath(__file__)
# script_dir = os.path.split(script_path)[0]
# file = "file.txt"
# abs_file_path = os.path.join(script_dir, file)
