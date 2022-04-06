import numpy as np
from operator import itemgetter

asteroids = []
station_asteroids_visible = []

length_field = 0
height_field = 0

def get_obstacles(_y_station,_x_station,_y_asteroid,_x_asteroid):

    divisors = [(_y_station,_x_station),(_y_asteroid,_x_asteroid)]
    obstacle = False

    if _x_station < _x_asteroid:
        steigung = (_y_asteroid - _y_station)/(_x_asteroid - _x_station)
        for j in range(_x_station + 1,_x_asteroid):
            y = _y_station + (j - _x_station) * steigung
            if y.is_integer() and y >= 0 and y < height_field:
                divisors.append((int(y), j, asteroids[int(y)][j]))
                if asteroids[int(y)][j] == '#':
                    obstacle = True

    elif _x_station > _x_asteroid:
        steigung = (_y_station - _y_asteroid)/(_x_station - _x_asteroid)
        for j in range(_x_asteroid+1,_x_station):
            y = _y_asteroid + (j - _x_asteroid) * steigung
            if y.is_integer() and y >= 0 and y < height_field:
                divisors.append((int(y), j, asteroids[int(y)][j]))
                if asteroids[int(y)][j] == '#':
                    obstacle = True
    
    elif _x_station == _x_asteroid:
        if _y_station < _y_asteroid:
            for y in range(_y_station + 1,_y_asteroid):
                if asteroids[int(y)][_x_station] == '#':
                    obstacle = True
        elif _y_station > _y_asteroid:
            for y in range(_y_asteroid + 1,_y_station):
                if asteroids[int(y)][_x_station] == '#':
                    obstacle = True

    return (obstacle)

def is_hidden(_y_station,_x_station,_y_asteroid,_x_asteroid):
    hidden = "*"
    if _x_station == _x_asteroid and _y_station == _y_asteroid:
        hidden = True
    else:
        hidden = get_obstacles(_y_station,_x_station,_y_asteroid,_x_asteroid)

    return hidden

def count_visible(_y,_x):
    count = 0

    for y in range(0,len(asteroids)):
        for x in range(0, len(asteroids[y])):
            if asteroids[y][x] == "#":
                test_hidden = is_hidden(_y,_x,y,x)
                if not test_hidden:
                    count += 1
                else:
                    pass

    return [count, _y, _x]

def check_asteroids(_asteroids):

    for i in range(0,len(_asteroids)):
        for j in range(0, len(_asteroids[i])):
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
