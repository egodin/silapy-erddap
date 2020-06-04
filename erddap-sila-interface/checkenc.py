#!/usr/bin/env python3
"""\
This script is displaying the encoding of files in the given path
usage: checkenc.py [-h] path
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""
# TODO:     1. generate output to log

__version__ = "1"

import argparse
import os

import chardet


def check_enc(data_path_dir):
    files = [
        f_name for f_name in os.listdir(data_path_dir)
        if f_name.endswith('.txt') or f_name.endswith('.csv')]

    for f_name in files:
        f_path = os.path.join(data_path_dir, f_name)
        with open(f_path, 'rb') as f:
            s = f.read()
        estimate = chardet.detect(s)
        for keys, val in estimate.items():
            if keys in 'encoding':
                print(f_name, '->', keys, ':', val, end=' ')
            if keys in 'confidence':
                print(keys, ':', val)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Enter the path to the dataset.")
    args = parser.parse_args()
    print(args.path)
    try:
        check_enc(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
