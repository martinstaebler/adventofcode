import numpy as np
import math

arr_input = []
arr_pattern = [0, 1, 0, -1]
number_of_loops = 100


arr_extended_pattern = []


def apply_pattern(_arr_input):
    arr_output = []

    for t in range(1, len(_arr_input)+1):
        arr_extended_pattern = []
        for r in range(0, len(_arr_input) + 1):
            arr_extended_pattern.append(arr_pattern[compute_pattern_index(r, t)])
        arr_multiply = np.array(_arr_input)
        arr_extended_pattern.remove(0)

        arr_output.append(int(str(np.sum(arr_multiply * arr_extended_pattern))[-1]))

    return arr_output

def compute_pattern_index(_arr_index, _row):
    index = int(_arr_index/_row)
    index = index - math.floor(index/4) * 4

    return index

def loops(_number_of_loops):
    global arr_input

    for a in range(0, _number_of_loops):
        arr_input = apply_pattern(arr_input)
        #print(arr_input)
    return arr_input

with open('adventofcode_1601_input.txt') as file:
    for line in file:
        for character in line:
            arr_input.append(int(character))


print("Ergebnis nach " + str(number_of_loops) + ": " +  str(loops(number_of_loops)))