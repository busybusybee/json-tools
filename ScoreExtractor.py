import json
import os
folder = "2021-10-05"
for i in os.listdir(folder):
    if i == "all":
        continue
    with open(os.path.join(folder,i,"scores.json")) as fp:
        myjson = json.load(fp)
    print(f"{i}\t{myjson['positioningScores']['flatPositioningError']}")
    # print(i)