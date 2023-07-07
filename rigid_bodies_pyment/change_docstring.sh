#!/bin/bash

# Path to the file containing the flag condition
flag_file="flag.txt"

# Read the flag condition from the file
run_condition=$(cat "$flag_file")

# Loop through all Python files in the directory
# for file in *.py; do
for file in rigid_body.py; do

    # Execute shell commands based on the flag condition
    if [ "$run_condition" = "True" ]; then
        # Execute commands for condition 1
        echo "Executing commands for condition 1 on file: $file"
        # Add your commands here
        pyment "$file"
        patch -p1 < "$file".patch

    else
        # Default condition or unknown flag
        echo "Docstring change condition is not set to True. Current flag set : $run_condition"
        # Add any default commands here
    fi
done
