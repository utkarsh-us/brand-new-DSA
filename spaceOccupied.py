# To measure the space taken by a Python file while it's running, you can use the `psutil` library. `psutil` provides information on system utilization, including memory and disk usage. You can monitor the disk usage before and after running your Python file to determine the space used. Here's how you can do it:

# First, you need to install the `psutil` library if you haven't already:


# bash #
# pip install psutil
 

# Then, create a Python program to measure the space taken by the Python file:

import os
import psutil

def get_file_size(file_path):
    # Get the size of the file in bytes
    file_size = os.path.getsize(file_path)
    return file_size

if __name__ == "__main__":
    print("File Size Measurement")
    print("Enter the path to the Python file you want to measure:")
    
    # Get the file path from the user
    file_to_measure = input()
    
    if os.path.isfile(file_to_measure):
        # Get the disk usage before running the Python file
        disk_usage_before = psutil.disk_usage('/')

        # Run the Python file
        os.system(f'python {file_to_measure}')

        # Get the disk usage after running the Python file
        disk_usage_after = psutil.disk_usage('/')

        # Calculate the space used during execution
        space_used = disk_usage_after.used - disk_usage_before.used
        print(f"The file '{file_to_measure}' used {space_used} bytes of space during execution.")
    else:
        print(f"The file '{file_to_measure}' does not exist or is not a valid file.")

# This program prompts the user for the path to the Python file, runs the file, and then calculates the disk space used before and after execution to determine the space used during the program's runtime.
