counter = 0
group = []



def compare_questions(arr_groups):
    return arr_groups[0].intersection(*arr_groups)

with open('aoc_2020_06_input.txt') as file:
    for line in file:
        stripped_line = line.strip()

        #print(len(stripped_line))
        if not len(stripped_line) == 0:
            group.append(set([x for x in stripped_line]))

        else:
            print(compare_questions(group))
            counter += len(compare_questions(group))
            print(group)
            group = []
    counter += len(compare_questions(group)) 

print(counter)
