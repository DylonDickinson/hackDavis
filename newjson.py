import json

import random
from io import StringIO



Courses =  json.load(open("/home/mchiao/Desktop/hackDavis/Courselist.json"))

names = ["Wellman Hall", "Olson Hall", "Giedt Hall", "Music Building", "Pritchard VMTH", "Valley Hall", "Walker Hall","Wright Hall", "Meyer Hall", "Sciences Lab Building", "Sproul Hall"]
sqft = [47563, 78526, 15540, 20204, 18500, 25000, 36740, 17000, 217503, 152646, 53875]

data = []

for i in Courses:
	dData = {
		"bldgName": "",
		"bldgSqft": 0,
		"startTime": 0,
		"endTime": 0,
		"numStudents": 0
	}
	seed = random.randint(-1,10)
	dData["bldgName"] = names[seed]
	dData["bldgSqft"] = sqft[seed]
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
