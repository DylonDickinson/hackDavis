from __future__ import division #gives floating point division
import folium
import os
import numpy as np
from folium.plugins import HeatMap
import json

jsonfile = json.load(open("./data.json")) #opens data.json

'''myList = [dic['startTime'] for dic in jsonfile if dic['startTime'] != None] #grabs times from json
endList = [dic['endTime'] for dic in jsonfile if dic['endTime'] != None]	#same thing
myList.extend(endList)
myList = list(sorted(set(myList)))''' #makes it into set, sorts, and then converts back to list

userTime = "20:00:00" #user input
totalStudents = [] #number of students, each element is a different building
ideal = 7 #ideal square ft per person
data = [] #data for map

def CalcWeight(students, sqft, ideal): #calculates the weight for heatmap
	ratio = float(sqft/students)
	weight = float(ideal/ratio)
	return weight

for course in jsonfile: #gets the data from json and inputs necessary data into data list
	if course['startTime'] == userTime or course['endTime'] == userTime:
		if len(data) == 0:
			totalStudents.append(course['numStudents'])
			data.append([course['lat'], course['lon'], CalcWeight(totalStudents[0], course['bldgSqft'],ideal)])
			continue
		for i in range(len(data)):
			if course['lat'] == data[i][0] and course['lon'] == data[i][1]:
				totalStudents[i] += course['numStudents']
				data[i][2] = CalcWeight(totalStudents[i], course['bldgSqft'], ideal)
				break
			else:
				totalStudents.append(course['numStudents'])
				data.append([course['lat'], course['lon'], CalcWeight(totalStudents[i+1], course['bldgSqft'],ideal)])

m = folium.Map(location=[38.541341, -121.751413], zoom_start = 17)

HeatMap(data, name ="Traffic", max_val = 1, radius=50).add_to(m)

m.save(os.path.join('results', 'map.html'))
