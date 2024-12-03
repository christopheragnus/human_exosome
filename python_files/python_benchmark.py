import subprocess
import unzip_downloads
import os
import time
import numpy as np

current_directory = os.getcwd()
list_of_times = []

for i in range(5):
  startTime = time.perf_counter()
  # terminal command to run the batch_download file
  command = ["python", "batch_download.py", "-f", f"{current_directory}/input/cls4-2.txt", "-p", "-o", "pdb_output_files"]

  result = subprocess.run(command, capture_output=True, text=True)

  print("Output of downloads")
  print(result.stdout)


  if result.stderr:
    print("Errors:")
    print(result.stderr)

  directory_path = "./pdb_output_files"
  unzip_downloads.unzip_gz_files(directory_path)
  
  endTime = time.perf_counter()
  duration = endTime - startTime
  list_of_times.append(duration)

  print(f"Time taken: {duration}")

print(f"List of compute times: {list_of_times}")


mean = np.mean(list_of_times)
std_dev = np.std(list_of_times)
two_std_dev = 2 * std_dev

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(f"Two Standard Deviations: {two_std_dev}")
print(f"Upper limit 2 std dev: {mean +  two_std_dev}")
print(f"Lower limit 2 std dev: {mean - two_std_dev}")