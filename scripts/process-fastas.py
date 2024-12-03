import os
import subprocess
import argparse

def run_alphafold_on_fasta_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it's a FASTA file
        if os.path.isfile(file_path) and file_name.endswith('.fasta'):
            # Construct the Alphafold command
            base_name = file_name.split('.')[0]
            output_dir = '/mnt/users/chris01/combfold-outputs'

            command = [
                'python3', '/mnt/scratch/alphafold/docker/run_docker.py',
                '--fasta_paths', file_path,
                '--max_template_date', '2022-01-01',
                '--data_dir', '/mnt/scratch/alphafold_ref/',
                '--output_dir', output_dir,
                '--model_preset', 'multimer',
                '--models_to_relax', 'all',
                '--gpu_devices', '1',
            ]
            
            # Run the command and capture the output
            result = subprocess.run(command, capture_output=True, text=True)
            
            # Print the standard output and standard error
            print(f"Output for {file_name}:")
            print(result.stdout)
            print(result.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Alphafold on all FASTA files in a folder")
    parser.add_argument('folder_path', type=str, help='Path to the folder containing FASTA files')
    
    args = parser.parse_args()
    run_alphafold_on_fasta_files(args.folder_path)
