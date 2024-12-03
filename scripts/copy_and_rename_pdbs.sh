
# Define the parent directory containing directories with .pdb files
parent_dir="/mnt/users/chris01/combfold-outputs-final"

# Define the destination directory where the renamed .pdb files will be copied
dest_dir="/mnt/users/chris01/pdbs"

# Loop through each directory in the parent directory
for dir in "$parent_dir"/*/; do
    # Extract the directory name (without the trailing slash)
    folder_name=$(basename "$dir")

    # Loop through each .pdb file in the current directory
    for pdb_file in "$dir"*.pdb; do
        # Check if any .pdb files exist
        if [ -e "$pdb_file" ]; then
            # Create a new file name with the folder name as a prefix
            new_file_name="${folder_name}_$(basename "$pdb_file")"
            
            # Copy the renamed file to the destination directory
            cp "$pdb_file" "$dest_dir/$new_file_name"
        fi
    done
done