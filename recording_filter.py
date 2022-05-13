'''
This script takes in a recording file and a csv and produces a recording that doesn't contain the beacons in the csv
'''


import os
import json
import csv
import pandas as pd

# myset = {2039, 2033}
# beacons = "/Users/nihatsen/Downloads/final_ major_minor_08_nov_2021.csv"
# with open(beacons) as fp:
#     spamreader = csv.reader(fp, delimiter=';', quotechar='|')
#     next(spamreader)
#     for row in spamreader:
#         myset.add(int(row[5]) - 65536)
# pass
# myset.add(44218 - 65536)
unwanted_majors = set(70, 71)
mydir = "/Users/nihatsen/Desktop/WorkWork/simulation-data/oamc"
# fileset = {
#     "BeaconSensorData_day-25-03-2022-time-14-51-28.json",
#     "BeaconSensorData_day-25-03-2022-time-15-00-00.json"
# }
files = [os.listdir(mydir)]
for record in files:
    try:
        # if(record not in fileset):
        #     continue
        path = os.path.join(mydir, record)
        newfilename = os.path.join(mydir, f"fixed_{record}")

        # record[0] == '.' or record.startswith('fixed') or os.path.isdir(path):
        if (not record.startswith('day')) or (not record.startswith('Beacon')):
            continue

        with open(path) as fp:
            myjson = json.load(fp)
        beacons_df = pd.DataFrame.from_records(myjson["beaconData"])
        # beacons_df = beacons_df[~(beacons_df["minor"].isin(myset))]
        # beacons_df = beacons_df[~((beacons_df["major"] == 6277) & (beacons_df["minor"] == -1611))]
        beacons_df = beacons_df[~beacons_df["major"].isin(unwanted_majors)]

        myjson["beaconData"] = beacons_df.to_dict('records')
        # with open(newfilename, "w+") as fp:
        with open(path, "w+") as fp:
            json.dump(myjson, fp)
    except Exception as e:
        print(e)
        pass
