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

def list_orbits_planet(_planet):
    orbit = _planet
    _li_orbits = []

    while orbit != "COM":
        orbit = (get_orbit(get_planet_index(orbit)))   
        _li_orbits.append(orbit) 

    return _li_orbits

def get_sum_transferorbits(_planet1, _planet2):
    _transfer_orbits_planet1 = []
    _transfer_orbits_planet2 = []
    orbits_planet1 = list_orbits_planet(_planet1)
    orbits_planet2 = list_orbits_planet(_planet2)

    _transfer_orbits_planet1 = [elem for elem in orbits_planet1 if elem not in orbits_planet2 ]
    _transfer_orbits_planet2 = [elem for elem in orbits_planet2 if elem not in orbits_planet1 ]

    return len(_transfer_orbits_planet1) + len(_transfer_orbits_planet2)

with open('./orbits.txt') as file:
    for line in file:
        li_orbits.append(line.strip().split(')'))

for item in li_orbits:
    set_orbit.add(item[1])

print("Anzahl der Transfer-Orbits: " + str(get_sum_transferorbits("YOU","SAN")))
