import numpy as np
import copy

report = []
report_rest = []


with open('aoc_2021_03_input.txt') as file:
    for line in file:
        report.append([int(x) for x in line.strip()])
    
    report_oxygen = copy.deepcopy(report)
    report_scrubber = copy.deepcopy(report)

    
    pos_count = 0
    bit = 0

    # oxygen
    while len(report_oxygen) > 1:
        report_flipped = np.transpose(report_oxygen).tolist()
        
        if sum(report_flipped[pos_count]) > len(report_flipped[pos_count]) / 2 or sum(report_flipped[pos_count]) == len(report_flipped[pos_count]) / 2: # mehr einsen
            bit = 1
        else:
            bit = 0
        report_rest = [x for x in report_oxygen if x[pos_count] == bit]
        report_oxygen = copy.deepcopy(report_rest)
        print(pos_count)
        pos_count += 1
    print("###")
    # CO2 scrubber
    pos_count = 0

    while len(report_scrubber) > 1:
        report_flipped = np.transpose(report_scrubber).tolist()
        
        if sum(report_flipped[pos_count]) > len(report_flipped[pos_count]) / 2 or sum(report_flipped[pos_count]) == len(report_flipped[pos_count]) / 2: # mehr einsen
            bit = 0
        else:
            bit = 1
        report_rest = [x for x in report_scrubber if x[pos_count] == bit]
        report_scrubber = copy.deepcopy(report_rest)
        print(pos_count)
        pos_count += 1

    
    print(int("".join([str(x) for x in report_oxygen[0]]), 2) * int("".join([str(x) for x in report_scrubber[0]]), 2))