import json
import os
for filename in sorted(os.listdir(os.curdir)):
    if not filename.startswith("fixed") and not filename.startswith("day") and not filename.startswith("Beacon"):
        continue
    with open(filename) as fp:
        myjson = json.load(fp)
    print(f"{filename} {myjson['optionalNotes']}")