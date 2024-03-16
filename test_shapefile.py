#!/bin/python3

import shapefile
import shapely.geometry as sg
import matplotlib.pyplot as plt
from alive_progress import alive_bar

file1 = "data/Shape Depts 41 45 89.shp"
file2 = "data/Shape Blois Orleans Auxerre.shp"
file3 = "data/Zones RURALES 41 45 89.shp"
file4 = "data/Zones URBAINES 41 45 89.shp"
file5 = "data/Zones PERI URBAINES 41 45 89.shp"

files = [file1,file2,file3,file4,file5]

for file in files: 
    print(file)
    r = shapefile.Reader(file)

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

import pickle
with open("grille.pkl", "rb") as fichier:
    objet_deserialise = pickle.load(fichier)
    json_data = objet_deserialise
    with alive_bar(len(json_data["grille"])) as bar:
        for entry in json_data["grille"]:
            x1,y1 = entry["s1_gps"]
            x2,y2 = entry["s2_gps"]
            x3,y3 = entry["s3_gps"]
            x4,y4 = entry["s4_gps"]
            
            x = [x1,x2,x3,x4]
            y = [y1,y2,y3,y4]

            plt.fill(x,y)
            bar()
plt.show()
