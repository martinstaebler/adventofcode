import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

moons_positions = []
moons_velocity = np.random.randint(1, size=(4,3))
unnoetig = "xyz=><,"
steps = 10000

def calculate_gravity(values):
    if values[0] > values[1]:
        gravity = -1
    elif values[0] < values[1]:
        gravity = 1
    else:
        gravity = 0

    return gravity

def apply_gravity():
    global moons_velocity

    for i in range(0,len(moons_velocity)):
        for j in range(0, len(moons_velocity[i])):
            for k in range(0,len(moons_velocity)):
                if i != k :
                    moons_velocity[i][j] += calculate_gravity(tuple((moons_positions[i][j],moons_positions[k][j])))

def apply_velocity():
    global moons_velocity
    global moons_positions
    moons_positions = moons_positions + moons_velocity

def get_total_energy():
    energy = 0

    for i in range(0,len(moons_positions)):
        energy += np.sum(abs(moons_positions[i])) * np.sum(abs(moons_velocity[i]))
    
    return energy

def time_steps(steps):
    pos_moon1 = [] 
    pos_moon2 = [] 
    pos_moon3 = [] 
    total_energy = []

    for i in range(0, steps):
        apply_gravity()
        apply_velocity()
        pos_moon1.append(moons_positions[0])
        pos_moon2.append(moons_positions[1])
        pos_moon3.append(moons_positions[2])
        total_energy.append(get_total_energy())
    
    pos_moon1 = np.array(pos_moon1)
    pos_moon1 = pos_moon1.reshape(3,-1)
    pos_moon2 = np.array(pos_moon2)
    pos_moon2 = pos_moon2.reshape(3,-1)
    pos_moon3 = np.array(pos_moon3)
    pos_moon3 = pos_moon3.reshape(3,-1)
    #print(pos_moon1)
    #ax.scatter(pos_moon1[0] ,pos_moon1[1] ,pos_moon1[2] ,zdir='z', s=1)
    #ax.scatter(pos_moon2[0] ,pos_moon2[1] ,pos_moon2[2] ,zdir='z', s=1)
    #ax.scatter(pos_moon3[0] ,pos_moon3[1] ,pos_moon3[2] ,zdir='z', s=2)

    x_range = np.arange(steps)
    plt.scatter(x_range, pos_moon1[0], s=1)

    print(moons_velocity)
    print(moons_positions)
    print(get_total_energy())
    plt.show()

with open('./adventofcode_1201_input.txt') as file:
    for line in file:
        line_stripped = line.strip()
        for char in unnoetig:
            line_stripped = line_stripped.replace(char, "")

        line_stripped = list(map(int, line_stripped.split()))
        moons_positions.append(line_stripped)
        
    moons_positions = np.array(moons_positions)

time_steps(steps)
