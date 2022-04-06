import numpy as np
import math
import copy
import time

signalmultiplier = 10000
loops = 100
arr_pattern = [0, 1, 0, -1]
arr_input = []
arr_output = []
value = 0

multiplied_string = ''

def compute_pattern_index(_arr_index, _row):
    # Multiplikationsfaktor für jeden Indexwert über eine Treppenfunktion berechnen
    index = int((_arr_index + 1)/_row)
    index = index - math.floor(index/4) * 4

    return index

with open('adventofcode_1601_input.txt') as file:

    for line in file:
        string = line.strip()
        for i in range(0, signalmultiplier):     #  -----> Hier wird der Input 10000 mal aneinandergehängt
            multiplied_string += string

        for character in multiplied_string:
            arr_input.append(int(character))

row = 1
input_length = len(arr_input)
start_time = time.time()

for t in range(0, loops):    #  -----> Anzahl der Loops
    print(f'loop {t}')
    arr_output = []
    for s in range(1, input_length + 1):
        print(f'zeile {s}')
        value = 0
        for a in range(s-1, input_length):
            #print(f'arr_input[a] {arr_input[a]} {arr_pattern[compute_pattern_index(a, s)]}')
            value += arr_input[a] * arr_pattern[compute_pattern_index(a, s)]
            #print(value)
        arr_output.append(int(str(value)[-1]))
        print(f'Dauer {time.time() - start_time}')
        start_time = time.time()
    arr_input = copy.deepcopy(arr_output)
    
print(arr_output)