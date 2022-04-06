import re

line_dict = {}
with open("aoc_2020_07_input.txt") as f:
    lines = f.readlines()

for x in lines:
    color = re.match('(.+?) bags', x).group(1)
    colors_inside = re.findall('(\d+) (.+?) bag', x)
    line_dict[color] = colors_inside

for key in line_dict:
    print(key, " : ", line_dict[key])
counter = 0
bag_arr = []


def open_bag(shiny_bag, bag_key):
    shiny_found = shiny_bag
    if line_dict[bag_key][0] == 1:
        return 1
    elif len(line_dict[bag_key]) == 0:
        return 0 
    else:
        for bag in line_dict[bag_key]:
            return open_bag(shiny_bag=shiny_bag, bag_key=bag)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
