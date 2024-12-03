import gzip 

import os
from pathlib import Path


def unzip_gz_files(directory):
  for filename in os.listdir(directory):
    if filename.endswith(".gz"):
       file_path = os.path.join(directory, filename)
       output_file_path = os.path.join(directory, filename[:-3])

       with gzip.open(file_path, "rb") as f_in:
         with open(output_file_path, "wb") as f_out:
          f_out.write(f_in.read())
        
       print(f"Unzipped {file_path} to {output_file_path}")
       




       


# with gzip.open('', "rb") as file_in:
#   with open("", "wb") as file_out;
#     shutil.copyfileobj(file_in, file_out)
#     print(f"{} file created")