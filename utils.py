import trimesh as tm
import numpy as np
from math import radians

def get_faces(mesh, min_=20, max_=23):
    for i, facet_area in enumerate(mesh.facets_area):
        if min_ < facet_area < max_:
            print(f"vertex index is: {i}", f"facet area is {facet_area}mm")
            print('{"facet": ' + str(i) +'}')
            mesh.visual.face_colors[mesh.facets[i]] = (0, 200, 0, 255)

def find_vertices(mesh, *args):
    li = []
    for i, (x, y, z) in enumerate(mesh.vertices):
        for value in args:
            if value == [x,y,z]:
                print(i)
                li.append(i)
    if len(li) == 1:
        print('{"vertex": ' + str(li[0]) + '}')
    else:
        print('{"vertex_list": ' + str(li) + '}')