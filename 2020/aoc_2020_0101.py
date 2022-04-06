

arr_numbers = []

def find_entries(numbers):
    set_numbers = set()
    for i in numbers:
        if 2020 - i in set_numbers:
            return (2020 - i) * i, i

        set_numbers.add(i)

with open('./aoc_2020_01_input.txt') as file:
    for line in file:
        arr_numbers.append(int(line.strip()))

print(find_entries(arr_numbers))
