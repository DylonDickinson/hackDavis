import time
import folium
from folium.plugins import HeatMap
from pathlib import Path
import json
import webbrowser


def main():

    ideal = 7  				 # ideal square ft per person
    weight_const = 5		 # adjust heat circle color separation
    bldg_foot_traffic = {}	 # store latitude, longitude, and amount of foot traffic for each building
    avg_lat = 0				 # average latitude of affected buildings
    avg_lon = 0				 # average longitude of affected buildings
    class_times = None       # contains input class data

    in_file = Path('input.txt')  # input data
    choose_time = Path('DavisHeatMap.html')  # uri to choose time
    heat_map = Path('map.html')  # uri to see map

    # opens input data
    with open('data.json') as data:
        class_times = json.load(data)

    webbrowser.open(choose_time.resolve().as_uri())

    # wait for input time from browser
    while not in_file.is_file():
        time.sleep(1)

    # read input time
    with open('input.txt') as input_file:
            user_time = input_file.read(8)

    # go through course schedule calculating foot traffic for each building
    for course in class_times:
        if course['startTime'] == user_time or course['endTime'] == user_time:

            # calculate a building's foot traffic value
            foot_traffic = ideal * course['numStudents'] / course['bldgSqft'] * weight_const
            if course['bldgName'] not in bldg_foot_traffic:
                avg_lat += course['lat']
                avg_lon += course['lon']
                bldg_foot_traffic[course['bldgName']] = [course['lat'], course['lon'], foot_traffic]
            else:
                bldg_foot_traffic[course['bldgName']][2] += foot_traffic

    avg_lat /= len(bldg_foot_traffic)
    avg_lon /= len(bldg_foot_traffic)

    # delete input file
    in_file.unlink()

    # set map at averaged position among buildings with traffic
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=17)

    # generate and save map file
    HeatMap(bldg_foot_traffic.values(), name='Traffic', max_val=1, radius=90, min_opacity=0.1).add_to(m)
    m.save('map.html')

    # open map
    webbrowser.open(heat_map.resolve().as_uri())


if __name__ == '__main__':
    main()
