import numpy as np
import math

arr_input = []
arr_input_multiplied = []
arr_pattern = list(map(int, [0, 1, 0, -1]))
arr_saved_pattern = []

number_of_loops = 100  # --------> Die ganze Berechnung wird 100 mal durchgeführt

arr_extended_pattern = []

def apply_pattern(_arr_input):
    # Multiplikation durchführen und berechnete Werte als Array zurückgeben

    arr_output = []
    length = len(_arr_input)
    
    for t in range(1, length + 1):
        print("zeile " + str(t))

        arr_multiply = np.asarray(_arr_input, dtype=int)
        arr_multiply_2 = np.asarray(compute_or_retrieve_pattern(t, length), dtype=int)

        arr_output.append(int(str(np.sum(arr_multiply * arr_multiply_2))[-1]))

    return arr_output

def compute_pattern_index(_arr_index, _row):
    # Multiplikationsfaktor für jeden Indexwert über eine Treppenfunktion berechnen
    index = int(_arr_index/_row)
    index = index - math.floor(index/4) * 4

    return index

def compute_or_retrieve_pattern(_row, _length):
    # Zeile des Patterns für die Multiplikation erstellen oder aus dem Array holen
    arr_extended_pattern = []

    if len(arr_saved_pattern) < _row + 1:
        for r in range(0, _length + 1):
            arr_extended_pattern.append(arr_pattern[compute_pattern_index(r, _row)])
        arr_extended_pattern.remove(0)
        #print(arr_extended_pattern)
        arr_saved_pattern.append(arr_extended_pattern)
    else:
        arr_extended_pattern = arr_saved_pattern[_row - 1]
    
    return arr_extended_pattern

def loops(_number_of_loops):
    global arr_input

    for a in range(0, _number_of_loops):
        print("loop " + str(a))
        arr_input = apply_pattern(arr_input)
        
    return arr_input

with open('adventofcode_1601_input.txt') as file:

    for line in file:
        string = line.strip()
        for character in string:
            arr_input.append(int(character))

    for i in range(0, 10000):     #  -----> Hier wird der Input 1000 mal aneinandergehägt
        arr_input_multiplied.append(arr_input)
    arr_input_multiplied = np.asarray(arr_input_multiplied, dtype=int)
    arr_input = arr_input_multiplied.reshape(-1,)
    #print(arr_input)

print("Ergebnis nach " + str(number_of_loops) + ": " +  str(loops(number_of_loops)))