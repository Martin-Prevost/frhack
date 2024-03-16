#!/bin/python3

import shapefile
import shapely.geometry as sg
import matplotlib.pyplot as plt
import sys

files = [
    "data/Shape Depts 41 45 89",
    "data/Shape Blois Orleans Auxerre"
    "data/Zones RURALES 41 45 89",
    "data/Zones URBAINES 41 45 89",
    "data/Zones PERI URBAINES 41 45 89"
]

#for file in files: 
#    print(file)
r = shapefile.Reader(sys.argv[1])

shape_obj = r.shapeRecords()[0]
geom = shape_obj.shape.__geo_interface__
for coord in geom["coordinates"]:
    datas = None
    if not isinstance(coord[0],list):
        datas = sg.Polygon(coord)
    else:
        datas = sg.Polygon(coord[0])
    x, y = datas.exterior.xy
    plt.plot(x, y)

plt.show()

