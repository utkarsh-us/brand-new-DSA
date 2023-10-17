import time
import subprocess

def measure_runtime(file_path):
    try:
        start_time = time.time()
        subprocess.run(["python", file_path], check=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Runtime of {file_path}: {elapsed_time:.2f} seconds")
    except subprocess.CalledProcessError:
        print("Error: The selected file did not run successfully.")

if __name__ == "__main__":
    file_path = input("Enter the path to the Python file: ")
    measure_runtime(file_path)


"""
 Python program that displays the runtime of any Python file selected, you can use the time module to measure the execution time of the selected script. You can use the time.time() function to record the start and end times and calculate the elapsed time. 

 In this program:

We import the time module to measure runtime and the subprocess module to run the selected Python script.

The measure_runtime function takes the path to the Python file as an argument.

Inside the function, we record the start time using time.time().

We use subprocess.run(["python", file_path], check=True) to run the selected Python script. The check=True parameter raises an exception if the script fails to run.

After the script execution is complete, we record the end time and calculate the elapsed time.

Finally, we print the runtime in seconds.

Make sure you have the Python interpreter installed and added to your system's PATH environment variable so that the subprocess.run command can execute Python scripts. This program allows you to measure the runtime of any Python script by providing its file path."""
