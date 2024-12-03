import os
import subprocess
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Run AlphaFold on a folder of FASTA files.")
parser.add_argument("--fasta_paths", required=True, help="Path to the folder containing FASTA files.")
parser.add_argument("--output_dir", required=True, help="Path to the output directory.")
args = parser.parse_args()

# Define directories
fasta_dir = args.fasta_paths
output_dir = args.output_dir
data_dir = "/mnt/scratch/alphafold_ref"

# Open log file
with open("log.txt", "w") as log_file:
    # Iterate over each FASTA file in the input directory
    for fasta_file in os.listdir(fasta_dir):
        if fasta_file.endswith(".fasta"):
            fasta_path = os.path.join(fasta_dir, fasta_file)
            command = [
                "python3", "/mnt/scratch/alphafold/docker/run_docker.py",
                "--fasta_paths", fasta_path,
                "--max_template_date", "2022-01-01",
                "--data_dir", data_dir,
                "--output_dir", output_dir,
                "--model_preset", "multimer"
            ]
            # Run the command and log the output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            log_file.write(f"Running command: {' '.join(command)}\n")
            for line in iter(process.stdout.readline, ''):
                print(line, end='')  # Print to console
                log_file.write(line)  # Write to log file
            stdout, stderr = process.communicate()
            log_file.write(stderr)
