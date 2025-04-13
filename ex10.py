"""
Exercise 10: Use the builtin modules, run dir command and print the filename and the datasize (edited)
"""
import os

def list_files():
    directory = os.getcwd()
    files = os.listdir(directory)
    for filename in files:
        if os.path.isfile(os.path.join(directory, filename)):
            full_path = os.path.abspath(filename)
            file_size = os.path.getsize(os.path.join(directory, filename))

            print(f"Filename: {filename}, Size: {file_size} bytes, Full Path: {full_path}")

print(list_files())