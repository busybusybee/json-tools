import json
import os

filter = {"beaconData", "sensorData", "gpsData"}
gaps = []
for filename in sorted(os.listdir(os.curdir)):
    if not filename.startswith("fixed") and not filename.startswith("day") and not filename.startswith("Beacon"):
        continue
    with open(filename) as source:
        myjson = json.load(source)
        for key, sect in myjson.items():
            if key not in filter:
                continue
            sect.sort(key=lambda x: x["timestamp"])
            for i in range(1,len(sect)):
                if sect[i]["timestamp"] > sect[i-1]["timestamp"] + 5:
                    time = sect[i]["timestamp"]
                    gaps.append((filename,key,sect[i-1]['timestamp'], sect[i]['timestamp'],
                                 sect[i]['timestamp'] - sect[i-1]['timestamp']))
if not gaps:
    print(f"No gaps found")
else:
    for gap in gaps:
        print(gap)

    print(f"Largest gap is {max(gaps,key=lambda x: x[4])}")
