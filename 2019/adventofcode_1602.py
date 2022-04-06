import numpy as np
import math

arr_input = []
arr_input_multiplied = []
arr_pattern = list(map(int, [0, 1, 0, -1]))
number_of_loops = 100


arr_extended_pattern = []


def apply_pattern(_arr_input):
    arr_output = []

    for t in range(1, len(_arr_input)+1):
        print("Zeile " + str(t))
        arr_extended_pattern = []
        for r in range(0, len(_arr_input) + 1):
            arr_extended_pattern.append(arr_pattern[compute_pattern_index(r, t)])
        #print("arr_extended_pattern " + str(arr_extended_pattern))
        arr_multiply = np.asarray(_arr_input, dtype=int)
        arr_extended_pattern.remove(0)

        arr_output.append(int(str(np.sum(arr_multiply * arr_extended_pattern))[-1]))

    return arr_output

def compute_pattern_index(_arr_index, _row):
    index = int(_arr_index/_row)

    while index > 3:
        index += -4 

    return index

def loops(_number_of_loops):
    global arr_input

    for a in range(0, _number_of_loops):
        print("Loop " + str(a))
        arr_input = apply_pattern(arr_input)
        
    return arr_input

with open('adventofcode_1602_input.txt') as file:
    for line in file:
        for character in line:
            arr_input.append(int(character))

    for i in range(0, 10):
        arr_input_multiplied.append(arr_input)
    arr_input_multiplied = np.asarray(arr_input_multiplied, dtype=int)
    arr_input = arr_input_multiplied.reshape(-1,)
    #print(arr_input_multiplied)

print("Ergebnis nach " + str(number_of_loops) + ": " +  str(loops(number_of_loops)))