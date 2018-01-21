from __future__ import division
import folium
import os
import numpy as np
from folium.plugins import HeatMap

ratio = float(47563/4000) #sqft / students
print ratio
weight = float(7/ratio)
print weight
#data = (np.random.normal(size=(100, 3)) *
#        np.array([[1, 1, 1]]) +
#        np.array([[48, 5, 1]])).tolist()
test = [38.541341, -121.751413, weight]
data = [test,[38.541641, -121.752055, weight]]
m = folium.Map(location=[38.541341, -121.751413], zoom_start = 17)
#m = folium.Map(location=[48., 5.], zoom_start = 25)
#print data
HeatMap(data, name ="Traffic").add_to(m)

m.save(os.path.join('results', 'map1.html'))
