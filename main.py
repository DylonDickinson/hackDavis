from __future__ import division #gives floating point division
import folium
import os, time
import numpy as np
from folium.plugins import HeatMap
import json
import webbrowser

jsonfile = json.load(open("./data.json")) #opens data.json

while not os.path.exists("/home/mchiao/Downloads/input.txt"): #change directory when testing on own computer
	time.sleep(1)

if os.path.isfile("/home/mchiao/Downloads/input.txt"): #make sure to change to own directory
		inputFile = open('/home/mchiao/Downloads/input.txt',"r")

'''myList = [dic['startTime'] for dic in jsonfile if dic['startTime'] != None] #grabs times from json
endList = [dic['endTime'] for dic in jsonfile if dic['endTime'] != None]	#same thing
myList.extend(endList)
myList = list(sorted(set(myList)))''' #makes it into set, sorts, and then converts back to list

userTime = inputFile.read(8) #user input

totalStudents = [] #number of students, each element is a different building
ideal = 7 #ideal square ft per person
data = [] #data for map

def CalcWeight(students, sqft, ideal): #calculates the weight for heatmap
	ratio = float(sqft/students)
	weight = float(ideal/ratio)
	return weight

def AvgLat(data):
	avg = 0
	for i in range(len(data)):
		avg += data[i][0]
	return float(avg/len(data))

def AvgLon(data):
	avg = 0
	for i in range(len(data)):
		avg += data[i][1]
	return float(avg/len(data))

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

os.remove("/home/mchiao/Downloads/input.txt") #deletes file from Downloads

m = folium.Map(
	location=[AvgLat(data), AvgLon(data)],
	zoom_start = 17
	)

HeatMap(data, name ="Traffic", max_val = 1, radius = 45).add_to(m)

m.save(os.path.join('results', 'map.html'))

webbrowser.open_new_tab("./results/map.html")
