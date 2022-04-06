arr_numbers = []

def find_entries(numbers):

    for i in numbers:
        for j in numbers:
             for k in numbers:
                if 2020 - i -j - k == 0:
                    return i * j * k

with open('./aoc_2020_01_input.txt') as file:
    for line in file:
        arr_numbers.append(int(line.strip()))

print(find_entries(arr_numbers))