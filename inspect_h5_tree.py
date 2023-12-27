"""
Displays the file structure of an HDF5 file (helper for MS-EVS dataset)
By default, the attributes are not displayed: use --verbose if needed.
This script comes without any guarantees.

Example usage:
    python inspect_h5_tree.py ./path/to/your/ms-evs/file.h5 --verbose
"""
import argparse
import h5py

def bold(string):
    return f"\033[1m{string}\033[0m"

def print_attributes(group, indent):
    """Print all attributes of an HDF5 group."""
    for name, attr in group.attrs.items():
        print("|   " * indent + "* " + f"{name} : {attr}")
        
def print_hdf5_tree(group, indent=0, verbose=False):
    """Recursively print the tree structure (and their attributes, if verbose) of an HDF5 group."""
    for name, item in group.items():
        if isinstance(item, h5py.Group):
            print("|   "*(indent) + bold(f"Group: {name}"))
        elif isinstance(item, h5py.Dataset):
            print("|   "*(indent) + bold(f"Dataset: {name}") + f" (Shape: {item.shape}, Dtype: {item.dtype})")
        else:
            print("|   "*(indent) + bold(f"Unknown item: {name}"))
        if verbose:
            print_attributes(group, indent)
        if isinstance(item, h5py.Group):
            print_hdf5_tree(item, indent + 1, verbose)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and display data from an HDF5 file (MS-EVS file structure).")
    parser.add_argument("file_path", type=str, help="Path to the HDF5 file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print attributes too")
    args = parser.parse_args()

    # Load HDF5 file
    with h5py.File(args.file_path, 'r') as file:
        print(f"File structure for {args.file_path}")
        print_hdf5_tree(file, verbose=args.verbose)
