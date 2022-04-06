import re

dict_bags = {}

set_bagswithgold = set()
set_emptybags = set()


with open("aoc_2020_07_input.txt") as file:
    for line in file:
        dict_bagsinbags = {}

        color = re.match('(.+?) bags contain', line).group(1)
        bags = re.findall('(\d+) (.+?) bag', line)
        for item in bags:
            dict_bagsinbags[item[1]] = int(item[0])

        dict_bags[color] = dict_bagsinbags


def resolve_bags():
    #for key_outer in dict_bags:
    max_num_bags = 2
    while max_num_bags > 1:
        max_num_bags = 0
        for key_inner in dict_bags:
            replace_bag(key_inner, dict_bags[key_inner])
            if len(dict_bags[key_inner]) > max_num_bags:
                max_num_bags = len(dict_bags[key_inner])

    for key in dict_bags:
        if "shiny gold" in dict_bags[key]:
            set_bagswithgold.add(key_inner)
        elif len(dict_bags[key]) == 0:
            set_emptybags.add(key)


def replace_bag(bag, dict_inner_bags):
    for key in dict_inner_bags:

        if key == "shiny gold":
            set_bagswithgold.add(bag)
        elif len(dict_bags[key]) == 0:
            set_emptybags.add(key)
        
    for item in set_emptybags:
        dict_bags[bag].pop(item, None)

    for item in set_bagswithgold:
        if item in dict_bags[bag]:
            amount_of_bags = dict_bags[bag][item]
            inner_golden_bags = dict_bags[item]["shiny gold"]
            if "shiny gold" in dict_bags[bag]:
                dict_bags[bag]["shiny gold"] = dict_bags[bag]["shiny gold"] + amount_of_bags * inner_golden_bags
            else:
                dict_bags[bag]["shiny gold"] = amount_of_bags * inner_golden_bags

            dict_bags[bag].pop(item)
            
resolve_bags()

for item in dict_bags:
    print(item, ":", dict_bags[item])

print("bags with gold", len(set_bagswithgold), len(dict_bags) - len(set_bagswithgold))
print("empty bags", len(set_emptybags), len(dict_bags) - len(set_emptybags))
print(len(dict_bags))
