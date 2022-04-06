
list_of_codes = []

with open("aoc_2020_08_input.txt") as file:
    for line in file:
        list_of_codes.append(line.strip().split(" "))

#print(list_of_codes)


def execute_code(codes):
    set_intructions = set()
    accumulator = 0
    old_accumulator = 0
    list_index = 0

    while 1 != 0:
        if list_index in set_intructions:
            return old_accumulator, accumulator, list_index
        else:
            set_intructions.add(list_index)
            old_accumulator = accumulator
            #print(list_of_codes[list_index][0], list_of_codes[list_index][1])
            if list_of_codes[list_index][0] == "jmp":
                list_index += int(list_of_codes[list_index][1])
            elif list_of_codes[list_index][0] == "acc":
                accumulator += int(list_of_codes[list_index][1])
                list_index += 1
            elif list_of_codes[list_index][0] == "nop":
                list_index += 1
        
        
            print("accumulator", accumulator, list_index)
            if accumulator == 5:
                return old_accumulator, accumulator

print(execute_code(list_of_codes))