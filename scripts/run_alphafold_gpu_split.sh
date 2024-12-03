#!/bin/bash

# Function to run AlphaFold on a specific FASTA file with a specified GPU
run_alphafold() {
  file_path=$1
  gpu_device=$2
  output_dir=$3
  base_name=$(basename "$file_path" .fasta)
  log_file="${output_dir}/${base_name}_alphafold.log"

  # Run AlphaFold process, show the output in terminal, and log it
  python3 -u /mnt/scratch/alphafold/docker/run_docker.py \
    --fasta_paths "$file_path" \
    --max_template_date 2022-01-01 \
    --data_dir /mnt/scratch/alphafold_ref/ \
    --output_dir "$output_dir" \
    --model_preset multimer \
    --models_to_relax best \
    --gpu_devices "$gpu_device" | tee "$log_file"

  echo "Finished AlphaFold for $file_path on GPU $gpu_device. Logs are saved in $log_file"
}

# Function to process a list of files on a specified GPU
process_files_on_gpu() {
  local gpu_device=$1
  shift
  local files=("$@")

  for file_path in "${files[@]}"; do
    if [[ -f "$file_path" ]]; then
      run_alphafold "$file_path" "$gpu_device" "$output_dir" &
    else
      echo "No FASTA files found: $file_path is not a regular file."
    fi
  done

  # Wait for all background processes for this GPU to finish
  wait
}

# Main function to iterate over all FASTA files in the folder and assign them to GPUs
run_alphafold_on_fasta_files() {
  folder_path=$1
  output_dir=$2
  files=("$folder_path"/*.fasta)  # Create an array of all FASTA files

  total_files=${#files[@]}  # Get total number of files

  if [[ $total_files -eq 0 ]]; then
    echo "No FASTA files found in the folder."
    exit 1
  fi

  half_files=$(( (total_files + 1) / 2 ))  # Divide the files, extra file to GPU 0 if odd

  # Split files into two groups
  files_gpu0=("${files[@]:0:half_files}")
  files_gpu1=("${files[@]:half_files}")

  echo "Assigning ${#files_gpu0[@]} files to GPU 0 and ${#files_gpu1[@]} files to GPU 1."

  # Start processing on GPU 0
  process_files_on_gpu 0 "${files_gpu0[@]}" &

  # Start processing on GPU 1
  process_files_on_gpu 1 "${files_gpu1[@]}" &

  # Wait for both GPU processes to finish
  wait

  echo "All AlphaFold runs completed on both GPUs."
}

# Ensure a folder path and output directory are provided as arguments
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <folder_path> <output_dir>"
  exit 1
fi

# Assign arguments to variables for clarity
folder_path="$1"
output_dir="$2"

# Create output directory if it doesn't exist
if [[ ! -d "$output_dir" ]]; then
  mkdir -p "$output_dir"
fi

# Run the main function with the provided folder path and output directory
run_alphafold_on_fasta_files "$folder_path" "$output_dir"

# Usage:
# ./run_alphafold_gpu_parallel.sh /path/to/fasta_folder /path/to/output_folder
