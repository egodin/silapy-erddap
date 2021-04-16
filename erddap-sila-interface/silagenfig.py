#!/usr/bin/env python3
"""\
This script is looping through all the files in a directory to generate a simple graph
to summarily evaluate the overall values of the table
usage: silagenfig.py [-h] path
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""

__version__ = "1"

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt


def genfig(data_path_dir):
    files = [
        f_name for f_name in os.listdir(data_path_dir)
        if f_name.endswith('.csv')]

    for f_name in files:
        f_sname = f_name + '.png'
        print('Preparing to save', f_sname, end=' ')
        f_path = os.path.join(data_path_dir, f_name)
        missing_values = ['-99999', '-99999.0']
        df = pd.read_csv(f_path, na_values=missing_values)
        df['time'] = pd.to_datetime(df['time'])
        df['measuredData'] = pd.to_numeric(df['measuredData'])
        plt.plot(df['time'], df['measuredData'])
        plt.title(f_name)
        plt.savefig(f_path + '.png')
        plt.close()
        print('OK')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Enter the path to the dataset.")
    args = parser.parse_args()
    print(args.path)
    try:
        genfig(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
