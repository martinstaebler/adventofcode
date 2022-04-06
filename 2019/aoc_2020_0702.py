import re

dict_bags = {}
list_allbags = []

with open("aoc_2020_07_input.txt") as file:
    for line in file:
        dict_bagsinbags = {}

        color = re.match('(.+?) bags contain', line).group(1)
        bags = re.findall('(\d+) (.+?) bag', line)
        for item in bags:
            dict_bagsinbags[item[1]] = int(item[0])

        dict_bags[color] = dict_bagsinbags

def resolve_bags():
    num_bags = 0
    counter = 0
    list_allbags = [{"shiny gold":1}]

    while len(list_allbags[counter]) > 0:

        list_allbags.append(replace_bag(list_allbags[counter]))
        
        num_bags += (sum([list_allbags[counter+1][key] for key in list_allbags[counter+1]]))
        print(list_allbags[counter+1], num_bags)
        counter += 1

    return num_bags


def replace_bag(dict_inner_bags):

    dict_replaced_bags = {}

    for key in dict_inner_bags:
        amount = dict_inner_bags[key]
 
        for innerkey in dict_bags[key]:
            if innerkey in dict_replaced_bags:
                dict_replaced_bags[innerkey] = dict_replaced_bags[innerkey] + amount * dict_bags[key][innerkey]
            else:
                dict_replaced_bags[innerkey] = amount * dict_bags[key][innerkey]
    return dict_replaced_bags

print("Number of bags", resolve_bags())
