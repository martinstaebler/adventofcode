arr_landscape = []

def count_trees(right, down):
    number_of_trees = 0

    toboggan_x = 0
    len_landscape_x = len(arr_landscape[0])

    for i in range(0, len(arr_landscape), down):

        value = arr_landscape[i][toboggan_x]

        if value.count("#") > 0:
            number_of_trees += 1
        toboggan_x += right
        if toboggan_x >= len_landscape_x:
            toboggan_x = toboggan_x - len_landscape_x
        
    return number_of_trees

with open('./aoc_2020_03_input.txt') as file:
    for line in file:
       arr_landscape.append(line.strip())
        


print(count_trees(3, 1))
print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))