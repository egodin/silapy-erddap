#!/usr/bin/env python3
"""\
This script is pushing variable and metadata information from the MODAAT metadata csv file to
the tomcat/content/erddap/datasets.xml ERDDAP file. The output is an xml file that can be validated
and then manually pasted in the main datasets.xml file.

usage: ./updatexml.py [-h] sourcefilename.
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""

import argparse
import pandas as pd

__version__ = "1"


def metadata_csvxmlconv(metadata_path):
    col_title = ['id', 'metadata', 'value']
    df = pd.read_csv(metadata_path, sep=';', header=None, usecols=[0, 1, 4], skiprows=1, names=col_title)



def main():
    parser = argparse.ArgumentParser(description='run to translate a reference metadata file to ERDDAP xml')
    parser.add_argument("path",
                        help="Enter the filename and its path. EX: /metadata/station_metadata.csv")
    args = parser.parse_args()
    try:
        metadata_csvxmlconv(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
