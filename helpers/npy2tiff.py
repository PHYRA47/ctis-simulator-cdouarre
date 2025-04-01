import numpy as np
import tifffile as tiff
import os

def convert_npy_to_tiff(npy_file, tiff_file):
    # Load the .npy file
    hsi_data = np.load(npy_file)
    
    # Save the data as a .tiff file
    tiff.imwrite(tiff_file, hsi_data)
    print(f"Converted {npy_file} to {tiff_file}")

def convert_all_npy_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".npy"):
            npy_file = os.path.join(input_directory, filename)
            tiff_file = os.path.join(output_directory, filename.replace(".npy", ".tiff"))
            convert_npy_to_tiff(npy_file, tiff_file)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert .npy HSI files to .tiff format.")
    parser.add_argument("input_directory", type=str, help="Directory containing .npy files to convert.")
    parser.add_argument("output_directory", type=str, help="Directory to save the converted .tiff files.")
    
    args = parser.parse_args()
    convert_all_npy_in_directory(args.input_directory, args.output_directory)

# Example usage:
# python helpers/npy2tiff.py <input_directory> <output_directory>