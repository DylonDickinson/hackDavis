import json
import random
from io import StringIO

Courses =  json.load(open("/home/mchiao/Desktop/hackDavis/Courselist.json"))

f = open("data.txt","w")

data = []
dData = {
	"startTime": 0,
	"endTime": 0,
	"numStudents": 0
}

for i in Courses:
	dData["startTime"] = i["Sections"][0]["Classtimes"][0]['StartTime']
	dData["endTime"] = i["Sections"][0]["Classtimes"][0]['EndTime']
	dData['numStudents'] = random.randint(14, 400)
	data.append(dData)
