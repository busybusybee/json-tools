import os
import json

filename = "day_2021_09_24_time_15_47_49_RecordedData.json"

with open(os.path.join(os.getcwd(), filename)) as fp:
    myjson = json.load(fp)
myjson["gpsData"] = [i for i in myjson["gpsData"] if i["timestamp"] < 300]
with open(f"fixed_{filename}", "w+") as fp:
    json.dump(myjson,fp)