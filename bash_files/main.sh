# File to store execution times
time_file="execution_times.txt"

# Directory containing .gz files
DIR=${1:-.}
echo $DIR

# Clear the time file at the start
> "$time_file"

file_name=$1
echo $file_name


# Function to measure time
measure_time() {
    start=$(date +%s.%N)  # Capture start time with nanosecond precision
    ./batch_download.sh -f "$file_name" -p -o "output"    # Run the script you want to measure
    extract_gz_files "$DIR"
    end=$(date +%s.%N)   # Capture end time
    echo "$(echo "$end - $start" | bc)" >> "$time_file"  # Store time in seconds
}

# Function to extract .gz files
extract_gz_files() {
    local dir=$1
    for file in output/*.gz; do
          echo "Extracting $file"
          gunzip -f "$file"
    done
}

# Repeat the script 5 times
for i in $(seq 1 5); 
do
    # echo $i
    measure_time
    cat $time_file
done

# Calculate the mean of execution times
mean_time=$(awk '{ sum += $1 } END { if (NR > 0) print sum / NR }' "$time_file")
echo "Average Execution Time: $mean_time seconds" 
echo "Average Execution Time: $mean_time seconds" >> 'mean_execution_time.txt'

