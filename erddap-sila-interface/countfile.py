#!/usr/bin/env python3
"""\
This script is counting the files per type in the given path
usage: countfile.py [-h] path
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""
# TODO:     1. generate output to log
#           2. add timestamp to output
#           3. add full path to output
#           4. comment the code

__version__ = "1"

import argparse
import os


def count_file(data_path_dir):
    txt_counter = 0
    csv_counter = 0
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(data_path_dir):
        for file in f:
            if '.txt' in file:
                txt_counter += 1
                files.append(os.path.join(r, file))
            if '.csv' in file:
                csv_counter += 1
                files.append(os.path.join(r, file))
    print(txt_counter, "*.txt files were detected in the designated folder...")
    print(csv_counter, "*.csv files were detected in the designated folder...")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Enter the path to the dataset.")
    args = parser.parse_args()
    print(args.path)
    try:
        count_file(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
