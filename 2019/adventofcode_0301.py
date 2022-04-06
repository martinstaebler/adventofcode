import matplotlib.pyplot as plt

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

def compare_coords(_coords1,_coords2):
    match_coords = []

    for element in _coords1:
        if element in _coords2:
            match_coords.append(element)
            print(element)

    return match_coords

def shortest_manhattan_distance(_coords):
    distances = []
    for tuple in _coords:
        distances.append(abs(tuple[0]) + abs(tuple[1]))

    distances.sort()
    return distances[0]

with open('./koordinaten_03.txt') as file:
    for line in file:
        wires.append(line.strip().split(','))

for element in wires[0]:
    vec_wire1.append(tuple((element[0],element[1:])))

for element in wires[1]:
    vec_wire2.append(tuple((element[0],element[1:])))

coords1 = vec_to_coords(vec_wire1)
coords2 = vec_to_coords(vec_wire2)

x_val_1 = [x[0] for x in coords1]
y_val_1 = [x[1] for x in coords1]

x_val_2 = [x[0] for x in coords2]
y_val_2 = [x[1] for x in coords2]

plt.plot(x_val_1,y_val_1)
plt.plot(x_val_2,y_val_2)
plt.show()

print(len(coords1))
print(len(coords2))

matching_coords = compare_coords(coords1, coords2)

print("Kürzeste Distanz einer Kreuzung: " + str(shortest_manhattan_distance(matching_coords)))