import json


pathList = {"logData" : "config\\aternosData.json", "contentData" : "config\\contentData.json"}

def getData(path, cat, obj):
    with open(pathList[path], "r") as f:
        data = json.loads(f.read())
        return data[cat][obj]



