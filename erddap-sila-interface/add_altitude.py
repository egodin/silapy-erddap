#!/usr/bin/env python3
"""\
This script is adding to ERDDAP ready file a column with the provided altitude. This
should not be run BEFORE sila2csv; sila2csv need to be run first, as the present function
cannot deal with the raw format made available from the SILA database.

usage: add_altitude.py [-h] path filename altitude
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""

import argparse
import os
import pandas as pd

__version__ = "1"


def set_altitude(data_path_dir, f_name, altitude):
    file_name = os.path.join(data_path_dir, f_name)
    df = pd.read_csv(file_name)
    df['altitude'] = altitude   # assigning altitude (float) as a constant to all records

    df.to_csv(os.path.join(data_path_dir, f_name),  # save to csv; overwriting (updating) original file
              index=False,
              encoding='utf-8',
              columns=['networkId', 'stationCode', 'latitude', 'longitude', 'altitude', 'time', 'subStationCode',
                       'qualityCode', 'measuredData'])


def main():
    parser = argparse.ArgumentParser(description='run after sila2csv on processed files to add a constant altitude '
                                                 'column to an ERDDAP ready datafile.')
    parser.add_argument("path",
                        help="Enter the path to the dataset. EX: /data/station")
    parser.add_argument("file_name",
                        help="Enter the data file name. EX: file.csv")
    parser.add_argument("altitude", type=float,
                        help="Enter the site altitude in decimal meters. EX: 25.0")
    args = parser.parse_args()
    try:
        set_altitude(args.path, args.file_name, args.altitude)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
