import json
import os
for filename in sorted(os.listdir(os.curdir)):
    if not (filename.startswith("fixed") or filename.startswith("day") or filename.startswith("Beacon")):
        continue
    mintime = 999999
    maxtime = 0
    with open(filename) as source:
        myjson = json.load(source)
        for sect,data in myjson.items():
            if not isinstance(data,list) or len(data) == 0:
                continue
            for elem in data:
                maxtime = max(elem["timestamp"], maxtime)
                mintime = min(elem["timestamp"], mintime)
    print(f"{filename}\t{int(maxtime//60)}:{int(maxtime % 60):02d}\t"
          f"{myjson['recordingInfo']['deviceModel'] if 'recordingInfo' in myjson.keys() else ''}\t{mintime}")
