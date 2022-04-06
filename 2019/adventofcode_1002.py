import numpy as np
from operator import itemgetter

asteroids = []
station_asteroids_visible = []

length_field = 0
height_field = 0

num_asteroids = 0
num_deleted = 0 

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
    hidden = False
    if _x_station == _x_asteroid and _y_station == _y_asteroid:
        hidden = True
    else:
        hidden = get_obstacles(_y_station,_x_station,_y_asteroid,_x_asteroid)

    return hidden

def count_visible(_y,_x):
    count = 0
    global num_asteroids
    num_asteroids = 0

    for y in range(0,len(asteroids)):
        for x in range(0, len(asteroids[y])):
            if asteroids[y][x] == "#":
                num_asteroids += 1
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

def get_manhattan_distance(_y1, _x1, _y2, _x2):
    distance = abs(_y2 - _y1) + abs(_x2 - _x1)
    return distance

def get_num_asteroids():
    num_asteroids = np.array(asteroids)
    #num_asteroids = ''.join(num_asteroids.reshape(1,-1))
    return num_asteroids

def sort_and_shoot(_coords_start, _coords_end, _coords_station):
    gradients = []
    last_gradient = None
    asteroids_deleted = 0
    global num_deleted

    for y in range(_coords_start[0],_coords_end[0]):
        for x in range(_coords_start[1],_coords_end[1]):
            if asteroids[y][x] == "#":
                if _coords_start[1]+1 == _coords_end[1]:
                    gradient = ""
                else:
                    gradient = (y - _coords_station[0])/(x - _coords_station[1])
                gradients.append((y, x, gradient, get_manhattan_distance(_coords_station[0], _coords_station[1], y, x)))

    for line in sorted(sorted(gradients, key=itemgetter(3)), key=itemgetter(2)):            
        if last_gradient != line[2]:
            asteroids[line[0]][line[1]] = "."
            asteroids_deleted += 1
            num_deleted += 1
            print(str(num_deleted) + " --> " + str(line[0]) + "," + str(line[1]))
            last_gradient = line[2]

    return asteroids_deleted

def start_vapor(_y_station, _x_station):
    global num_asteroids
    global num_deleted
    num_deleted = 0

    print(num_asteroids)
    while num_asteroids > 1:
        # Nord
        num_asteroids = num_asteroids - sort_and_shoot(tuple((0,_x_station)), tuple((_y_station,_x_station+1)), tuple((_y_station, _x_station)))
        # Östliche Hemisphäre
        num_asteroids = num_asteroids - sort_and_shoot(tuple((0,_x_station+1)), tuple((len(asteroids),len(asteroids[0]))), tuple((_y_station, _x_station)))
        # Süd
        num_asteroids = num_asteroids - sort_and_shoot(tuple((_y_station+1,_x_station)), tuple((len(asteroids),_x_station+1)), tuple((_y_station, _x_station)))
        # Westliche Hemisphäre
        num_asteroids = num_asteroids - sort_and_shoot(tuple((0,0)), tuple((len(asteroids),_x_station)), tuple((_y_station, _x_station)))

    for line in asteroids:
        print(line)

with open('./asteroids_10.txt') as file:
    for line in file:
        line_stripped = line.strip()
        asteroids.append([(line_stripped[i:i+1]) for i in range(0, len(line_stripped), 1)])

length_field = len(asteroids)
height_field = len(asteroids[0])

check_asteroids(asteroids)

station_asteroids_visible = sorted(station_asteroids_visible, key=itemgetter(0))

start_vapor(station_asteroids_visible[-1][1],station_asteroids_visible[-1][2])

