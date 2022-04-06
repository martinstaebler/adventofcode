import numpy as np

report = []

gamma, epsilon = "", "" 

with open('aoc_2021_03_input.txt') as file:
    for line in file:
        report.append([int(x) for x in line.strip()])
    report_flipped = np.transpose(report).tolist()

    for element in report_flipped:
        if sum(element) > len(element) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2) * int(epsilon, 2))