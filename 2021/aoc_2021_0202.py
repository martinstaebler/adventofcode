vertical, horizontal, aim = 0, 0, 0

with open('aoc_2021_02_input.txt') as file:
    for line in file:
        move = line.strip().split()


        if move[0] == 'forward':
            horizontal += int(move[1])
            vertical += aim * int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])
        elif move[0] == 'down':
            aim += int(move[1])
        
          

    print(vertical * horizontal)
                