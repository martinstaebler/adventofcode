import re


counter = 0

with open('./aoc_2020_02_input.txt') as file:
    for line in file:
        #print(re.split('[- :\\s]+', line.strip()))
        input = re.split('[- :\\s]+', line.strip())
        
        password = input[3]
        if (password[int(input[0])-1] == input[2]) ^ (password[int(input[1])-1] == input[2]):
            counter += 1


print(counter)