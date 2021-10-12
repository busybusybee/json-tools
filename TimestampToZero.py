import json
import os
for filename in os.listdir(os.curdir):
    if not filename.startswith("Beacon"):
        continue
    with open(filename) as source:
        myjson = json.load(source)
        mintime = myjson["sensorData"][0]["timestamp"]
        maxtime = 0
        for name, sect in myjson.items():
            if not isinstance(sect, list):
                continue
            for i in sect:
                mintime = min(mintime, i["timestamp"])
                maxtime = max(maxtime, i["timestamp"])
        print(mintime)
        print(maxtime)
        print(maxtime-mintime)
        # for name, sect in myjson.items():
        #     if not isinstance(sect, list):
        #         continue
        #     for i in range(len(sect)):
        #         sect[i]["timestamp"] -= mintime
        for i, elem in enumerate(myjson["sensorData"]):
            myjson["sensorData"][i]["timestamp"] -= mintime
        with open(f"fixed_{filename}", "w") as newfile:
            json.dump(myjson, newfile)
