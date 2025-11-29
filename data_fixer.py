import gzip
import os

# 1. Define paths for the corrupted input and the temporary fixed output
corrupt_file = "data/iMKd7/matrix.mtx.gz"
fixed_file = "data/iMKd7/matrix_fixed.mtx.gz"
temp_data_file = "data/iMKd7/temp_body.txt"

print(f"Starting repair process for file: {corrupt_file}")

valid_lines_count = 0
header_lines = []

try:
    # Use gzip module to stream read/write
    with gzip.open(corrupt_file, 'rt') as f_in:
        # Read the first two header lines (%%MatrixMarket... and %metadata...)
        header_1 = f_in.readline()
        header_2 = f_in.readline()
        
        # Read the third line (dimensions), which is the target for correction
        dim_line = f_in.readline()
        
        # Original dimensions: rows, cols, total_expected_count
        try:
            rows, cols, total_expected = dim_line.strip().split()
            print(f"Original declared entry count: {total_expected}")
        except ValueError:
            print("Error: Could not parse dimension line. The file might be severely corrupted.")
            raise

        # Strategy to handle large files without memory overflow:
        # 1. Iterate through the body, writing valid lines to a temporary text file.
        # 2. Count valid lines during this pass.
        # 3. Write the final file combining: Header + Corrected Dimensions + Temp Body.
        
        print("Cleaning data body (removing corrupted/garbage lines)...")
        
        with open(temp_data_file, 'w') as f_temp:
            for line in f_in:
                # Core logic: Only lines starting with a digit are considered valid data
                if line and line[0].isdigit():
                    try:
                        # Verify the line contains exactly 3 parts (row, col, value)
                        parts = line.split()
                        if len(parts) == 3:
                            # Valid line found, write to temp file
                            f_temp.write(line)
                            valid_lines_count += 1
                    except ValueError:
                        # Parsing failed, likely reached the corruption boundary
                        break 
                else:
                    # Non-digit start indicates corruption or EOF
                    break 
    
    print(f"Cleaning complete. Actual valid entries: {valid_lines_count}")
    
    # Calculate data loss statistics
    loss = int(total_expected) - valid_lines_count
    loss_pct = 100 * loss / int(total_expected)
    print(f"Entries lost: {loss} ({loss_pct:.4f}%)")

    # 2. Assemble the final fixed file
    print("Generating final fixed file...")
    
    with gzip.open(fixed_file, 'wt') as f_final:
        # Write original headers
        f_final.write(header_1)
        f_final.write(header_2)
        
        # Write corrected dimension line (rows, cols, NEW_count)
        f_final.write(f"{rows} {cols} {valid_lines_count}\n")
        
        # Append content from the temporary data file
        with open(temp_data_file, 'r') as f_temp:
            for line in f_temp:
                f_final.write(line)
    
    # 3. Replace the original file safely
    # Rename the original file to .bak before replacing it with the fixed version
    if os.path.exists(corrupt_file + ".bak"):
        os.remove(corrupt_file + ".bak")
        
    os.rename(corrupt_file, corrupt_file + ".bak")
    os.rename(fixed_file, corrupt_file)
    
    # Cleanup temporary file
    if os.path.exists(temp_data_file):
        os.remove(temp_data_file)
    
    print(f"✅ Repair successful! Original file backed up to: {corrupt_file}.bak")
    print("You may now restart the kernel and run your analysis code.")

except Exception as e:
    print(f"An error occurred during the repair process: {e}")
