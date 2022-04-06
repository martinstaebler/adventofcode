li_orbits = []
set_orbit = set()

def get_orbit(_index):
    return li_orbits[_index][0]

def get_planet_index(_planet):
    for i in range(0, len(li_orbits)):
        if _planet in li_orbits[i][1]:
            index = i
            break
    return index

def count_orbits(_set):
    sum_orbits = 0

    for item in _set:
        orbit = item

        while orbit != "COM":
            orbit = (get_orbit(get_planet_index(orbit)))   
            sum_orbits += 1 

    return sum_orbits

with open('./orbits.txt') as file:
    for line in file:
        li_orbits.append(line.strip().split(')'))

for item in li_orbits:
    set_orbit.add(item[1])

print("Anzahl der Orbits: " + str(count_orbits(set_orbit)))


