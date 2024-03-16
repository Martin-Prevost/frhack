#!/bin/python3

import shapefile
import shapely.geometry as sg
import matplotlib.pyplot as plt
import sys

r = shapefile.Reader(sys.argv[1])

shape_obj = r.shapeRecords()[0]
geom = shape_obj.shape.__geo_interface__
for coord in geom["coordinates"]:
    datas = sg.Polygon(coord[0])
    x, y = datas.exterior.xy

    plt.plot(x, y)
plt.show()

