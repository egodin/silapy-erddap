#!/usr/bin/env python3
"""\
This script is sanitizing the SILA files to make it ready for ERDDAP csv
usage: sila2csv.py [-h] path
Author: Etienne Godin
Author email: etienne.godin@cen.ulaval.ca
"""
# TODO:     1. generate output to log
#           2. add timestamp to output
#           3. add full path to output
#           4. comment the code
#           5. make UTC offset addition parameterizable when running the program. Default to UTC
#           6. make SILA network name as parameterizable when running the program. Default to empty
#           7. implement rounding [pandas.DataFrame.round] before df.to_csv
#           8. add output folder capabilities to argparse
#           9. time: formatting is hardcoded, consider making function(arguments)

__version__ = "1"

import argparse
import os
import pandas as pd

SILA_widths = [5, 7, 9, 9, 13, 20, 2, 8]


def sila2csvconv(data_path_dir):
    files = [
        f_name for f_name in os.listdir(data_path_dir)
        if f_name.endswith('.txt') or f_name.endswith('.csv')]

    for f_name in files:
        f_path = os.path.join(data_path_dir, f_name)
        df = pd.read_fwf(f_path, widths=SILA_widths, header=None, converters={0: str, 2: str, 3: str})
        df.columns = ['dataCode', 'stationCode', 'latitude', 'longitude', 'time', 'subStationCode', 'qualityCode',
                      'measuredData']
        df['networkId'] = 'SILA'  # set network name id
        df['time'] = df['time'].astype(str) + '-5:00'  # set UTC offset

        lat_units = df.latitude.str[:4]  # set decimals for latitude
        lat_dec = df.latitude.str[4:]
        lat = lat_units + '.' + lat_dec
        df['latitude'] = lat

        long_units = df.longitude.str[:4]  # set decimals for longitude
        long_dec = df.longitude.str[4:]
        long = long_units + '.' + long_dec
        df['longitude'] = long

        str_time_year = df.time.str[0:4]  # format time
        str_time_month = df.time.str[4:6]
        str_time_day = df.time.str[6:8]
        str_time_hour = df.time.str[9:11]
        str_time_minute = df.time.str[11:13]
        str_time_zone = df.time.str[13:18]
        time_formatted = (str_time_year + '-' +
                          str_time_month + '-' +
                          str_time_day + 'T' +
                          str_time_hour + ':' +
                          str_time_minute + ':00' +
                          str_time_zone)
        df['time'] = time_formatted

        base_name = os.path.splitext(f_name)[0]  # rename the processed file
        print('Sanitizing', f_name, '->', end=' ')
        f_name = base_name + '_erddap' + '.csv'
        print(f_name)
        df.to_csv(os.path.join(data_path_dir, f_name),  # save to csv
                  index=False,
                  encoding='utf-8',
                  columns=['networkId', 'dataCode', 'stationCode', 'latitude', 'longitude', 'time', 'subStationCode',
                           'qualityCode', 'measuredData'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Enter the path to the dataset.")
    args = parser.parse_args()
    print(args.path)
    try:
        sila2csvconv(args.path)
    except():
        print('Invalid path or no datasets found.')


if __name__ == "__main__":
    main()
