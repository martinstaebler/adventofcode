import numpy as np
from operator import itemgetter

asteroids = []
station_asteroids_visible = []

length_field = 0
height_field = 0

def berechne_steigung(_y_station,_x_station,_y_asteroid,_x_asteroid):
    steigung = ""

    if _x_station < _x_asteroid:
        steigung = str((_y_asteroid - _y_station)/(_x_asteroid - _x_station)) + "rechts"

    elif _x_station > _x_asteroid:
        steigung = str((_y_station - _y_asteroid)/(_x_station - _x_asteroid)) + "links"
    
    elif _x_station == _x_asteroid:
        if _y_station < _y_asteroid:
            steigung = "inf_unten"

        elif _y_station > _y_asteroid:
            steigung = "inf_oben"

    return steigung

def count_visible(_y,_x):
    set_steigung = set()
    for y in range(0,length_field):
        for x in range(0, height_field):
            if asteroids[y][x] == "#":
                if _x == x and _y == y:
                    pass
                else:
                    set_steigung.add(berechne_steigung(_y,_x,y,x))

    return [len(set_steigung), _y, _x]

def check_asteroids(_asteroids):

    for i in range(0,length_field):
        for j in range(0, height_field):
            if _asteroids[i][j] == '#':
               station_asteroids_visible.append(count_visible(i,j))

with open('./asteroids_10.txt') as file:
    for line in file:
        line_stripped = line.strip()
        asteroids.append([(line_stripped[i:i+1]) for i in range(0, len(line_stripped), 1)])

length_field = len(asteroids)
height_field = len(asteroids[0])

check_asteroids(asteroids)

station_asteroids_visible = sorted(station_asteroids_visible, key=itemgetter(0))

print(station_asteroids_visible)
