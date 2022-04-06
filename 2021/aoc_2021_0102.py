sonar_list = []
increased_count = 0

with open('aoc_2021_01_input.txt') as file:
    for line in file:
        sonar_list.append(int(line))

for i in range(3, len(sonar_list)):

    if sum(sonar_list[i-3:i]) < sum(sonar_list[i-2:i+1]):
        increased_count += 1

print(increased_count)