matching_coords = [[227, 0],
[561, 0],
[723, -842],
[675, -1040],
[997, -1227],
[997, -1007],
[926, -1434],
[926, -1467],
[838, -1612],
[891, -2455],
[838, -2262],
[-2298, -1219],
[-2298, -948],
[-2153, -941],
[-1654, -411],
[-1094, -462],
[-682, -601],
[-1094, -823],
[-1351, -823],
[-1077, -183],
[-678, -183],
[-626, -188],
[-626, -262],
[-626, -456],
[-626, -601],
[-1094, -857],
[-1351, -857],
[-1443, -948],
[-1443, -954],
[-900, -601],
[-1094, -500],
[-1517, -500],
[-1570, -411]]


wires = []
vec_wire1 = []
vec_wire2 = []

def vec_to_coords(vectors):
    pos_x = 0
    pos_y = 0
    coords = []
    for tuple in vectors:
        if tuple[0] == "R":
            for i in range(0,int(tuple[1])):
                pos_x += 1
                coords.append([pos_x,pos_y])

        elif tuple[0] == "L":
            for i in range(0,int(tuple[1])):
                pos_x -= 1
                coords.append([pos_x,pos_y])

        elif tuple[0] == "U":
            for i in range(0,int(tuple[1])):
                pos_y += 1
                coords.append([pos_x,pos_y])

        elif tuple[0] == "D":
            for i in range(0,int(tuple[1])):
                pos_y -= 1
                coords.append([pos_x,pos_y])
        
    return coords

def min_steps_to_coords(_coords1, _coords2, _matching_coords):
    steps = []
    for element in _matching_coords:
        steps.append(_coords1.index(element) + _coords2.index(element) + 2)
    steps.sort()
    return steps[0]

def compare_coords(_coords1,_coords2):
    match_coords = []

    for element in _coords1:
        if element in _coords2:
            match_coords.append(element)
            #print(element)

    return match_coords

with open('./koordinaten_03.txt') as file:
    for line in file:
        wires.append(line.strip().split(','))

for element in wires[0]:
    vec_wire1.append(tuple((element[0],element[1:])))

for element in wires[1]:
    vec_wire2.append(tuple((element[0],element[1:])))

coords1 = vec_to_coords(vec_wire1)
coords2 = vec_to_coords(vec_wire2)

print("Wenigste Schritte zu einer Kreuzung: " + str(min_steps_to_coords(coords1, coords2, matching_coords)))