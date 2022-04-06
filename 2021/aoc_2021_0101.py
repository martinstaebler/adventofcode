sonar_list = []
increased_count = 0

with open('aoc_2021_01_input.txt') as file:
    for line in file:
        sonar_list.append(int(line))
    
for i in range(1, len(sonar_list)):
    if sonar_list[i-1] < sonar_list[i]:
        increased_count += 1

print(increased_count)