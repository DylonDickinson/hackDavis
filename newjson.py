import json

import random
from io import StringIO

Courses =  json.load(open("./Courselist.json"))

names = ["Wellman Hall", "Olson Hall", "Giedt Hall", "Music Building", "Pritchard VMTH", "Valley Hall", "Walker Hall","Wright Hall", "Meyer Hall", "Sciences Lab Building", "Sproul Hall"]
sqft = [47563, 78526, 15540, 20204, 18500, 25000, 36740, 17000, 217503, 152646, 53875]
lat = [38.541341, 38.540031, 38.537818, 38.539157, 38.532072, 38.532817, 38.539753, 38.538780, 38.534848, 38.539805, 38.540037]
lon = [-121.751413, -121.747593, -121.755670, -121.747361,-121.764248, -121.763708,-121.750775, -121.747899,-121.754408, -121.754833, -121.746887]

data = []

for i in Courses:
	dData = {
		"bldgName": "",
		"bldgSqft": 0,
		"lat": 0.0,
		"lon": 0.0,
		"startTime": 0,
		"endTime": 0,
		"numStudents": 0
	}
	seed = random.randint(-1,10)
	dData["bldgName"] = names[seed]
	dData["bldgSqft"] = sqft[seed]
	dData["lat"] = lat[seed]
	dData["lon"] = lon[seed]
	if i["Sections"][0]["Classtimes"][0]['StartTime'] != None:
		for sec in i["Sections"]: #come back to this. fix for multiple sections
			dData["startTime"] = sec["Classtimes"][0]['StartTime']
			dData["endTime"] = sec["Classtimes"][0]['EndTime']
			if dData["bldgSqft"] <= 25000:
				dData['numStudents'] = random.randint(55, 350)
			elif dData["bldgSqft"] <= 50000:
				dData['numStudents'] = random.randint(150, 500)
			elif dData["bldgSqft"] <= 79000:
				dData['numStudents'] = random.randint(200, 575)
			else: dData['numStudents'] = random.randint(300, 750)
		data.append(dData)

with open("data.json", "w") as fp:
	json.dump(data, fp, indent=4)
