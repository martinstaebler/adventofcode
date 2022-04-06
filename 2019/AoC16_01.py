import time

signal = []

with open('adventofcode_1601_input.txt') as file:
    for line in file:
        for character in line:
            signal.append(int(character))

signal_index_max = len(signal)
loop_max = 100
time_start = time.perf_counter()
base_pattern = [ 0, 1, 0, -1]

# Loops
for loop in range(0,loop_max):
    # Signal parsing
    for signal_index in range(signal_index_max):
        # Pattern scaling depending on index
        pattern_index = 0
        summe = 0
        pattern_loop = 0
        pattern_state = 0
        arithPointer = signal_index
        # start adding the multiplication of each single signal element based on the base_pattern index
        while arithPointer < signal_index_max:
            # skip first math
            if arithPointer == signal_index and pattern_state == 0:
                pattern_index = 1
                # at the very beginning also push the state
                if signal_index == 0:
                    pattern_state = 1
            # do the math
            summe += signal[arithPointer] * base_pattern[pattern_index]
            # state check and appropriate pattern_index inc
            if pattern_state == 0:
                if pattern_loop > signal_index:
                    pattern_state = 1
                    pattern_loop = 0
                else:
                    pattern_loop += 1
            elif pattern_state == 1:
                if pattern_loop > signal_index:
                    pattern_state = 2
                    pattern_loop = 0
                else:
                    pattern_loop += 1
            elif pattern_state == 2:
                if pattern_loop > signal_index:
                    pattern_state = 3
                    pattern_loop = 0
                else:
                    pattern_loop += 1
            elif pattern_state == 3:
                if pattern_loop > signal_index:
                    pattern_state = 0
                    pattern_loop = 0
                else:
                    pattern_loop += 1
            # Pointer of next base pattern value, in this case applies pattern_index == pattern_state
            pattern_index = pattern_state
            # Pointer of next value to do math with
            arithPointer += 1
        # write new value
        signal[signal_index] = summe % 10
    print(f'Loop# {loop} completed after {round(time.perf_counter()-time_start, 2)} second(s)')
    print(signal)
