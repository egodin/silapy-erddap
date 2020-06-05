#!/usr/bin/env python3
"""\
This script is the encoding the files in the given path to UTF-8 [unix] using dos2unix
usage: encode.py [-h] path
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
import subprocess


def encode_utf8(data_path_dir):
    files = [
        f_name for f_name in os.listdir(data_path_dir)
        if f_name.endswith('.txt') or f_name.endswith('.csv')]

    for f_name in files:
        f_path = os.path.join(data_path_dir, f_name)
        subprocess.call(["dos2unix", f_path])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Enter the path to the dataset.")
    args = parser.parse_args()
    print(args.path)
    try:
        encode_utf8(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
