import re


counter = 0

with open('./aoc_2020_02_input_tanja.txt') as file:
    for line in file:
        #print(re.split('[- :\\s]+', line.strip()))
        input = re.split('[- :\\s]+', line.strip())
        char_count = input[3].count(input[2])
        if int(input[0]) <= char_count <= int(input[1]):
            counter += 1


print(counter)
