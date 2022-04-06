import numpy as np

moons_positions = []
moons_velocity = np.random.randint(1, size=(4,3))
unnoetig = "xyz=><,"

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
    for i in range(0, steps):
        apply_gravity()
        apply_velocity()

    print(moons_velocity)
    print(moons_positions)
    print(get_total_energy())

with open('./adventofcode_1201_input.txt') as file:
    for line in file:
        line_stripped = line.strip()
        for char in unnoetig:
            line_stripped = line_stripped.replace(char, "")

        line_stripped = list(map(int, line_stripped.split()))
        moons_positions.append(line_stripped)
        
    moons_positions = np.array(moons_positions)

time_steps(1000)
