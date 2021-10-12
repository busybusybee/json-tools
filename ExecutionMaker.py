import json

with open("New Arrival Airside Checkpoints.json") as source:
    mylist = json.load(source)[0]["nodeData"]
newlist = [{"nodeIdentifier": elem["nodeIdentifier"], "visitTimestampUtcEpochSeconds": elem["timestamp"]}
           for elem in mylist]
with open("BaseExecution.json") as base:
    newjson = json.load(base)

newjson["positionScoringPlanIdentifier"] = "Plan1"
newjson["executionStarttimeUtcEpochSeconds"] = newlist[0]["visitTimestampUtcEpochSeconds"]
newjson["executionEndtimeUtcEpochSeconds"] = newlist[-1]["visitTimestampUtcEpochSeconds"]
newjson["assetData"]["assetMacIdentifier"] = "f7:74:9f:74:4b:04"
newjson["assetData"]["executionData"] = newlist

with open("newExecution.json", 'w') as newfile:
    json.dump(newjson, newfile, indent=2)
