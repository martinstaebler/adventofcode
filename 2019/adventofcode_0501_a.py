lst, param, ptr, skip = [int(i) for i in open('./air_conditioner_05.txt').read().split(',')], {}, 0, (4,4,2,2,3,3,4,4)

while lst[ptr] is not 99:
    opcode = lst[ptr] % 100
    print("arrayindex " + str(ptr) + " -> Inhalt: " + str(lst[ptr]) +  " -> opcode: " + str(opcode))

    for i in range(1,4): 
        param[i] = ptr + i if lst[ptr]//int('100'.ljust(i+2, '0')) % 10 else lst[ptr + i]
        #print("param[" + str(i) + "] " + str(param[i]))
    if opcode is 1: 
        lst[param[3]] = lst[param[1]] + lst[param[2]]
    elif opcode is 2: 
        lst[param[3]] = lst[param[1]] * lst[param[2]]
    elif opcode is 3: 
        lst[param[1]] = int(input('1 or 5?: '))
    elif opcode is 4: 
        print("4: " + str(lst[param[1]]))
    elif opcode is 5 and lst[param[1]] or opcode is 6 and not lst[param[1]]: 
        ptr = lst[param[2]] - 3
        print("5 --->  param[1] " + str(param[1]) + " param[2] " + str(param[2]) + " ptr " + str(ptr + 3))
    elif opcode is 7: 
        lst[param[3]] = 1 if lst[param[1]] < lst[param[2]] else 0
    elif opcode is 8: 
        lst[param[3]] = 1 if lst[param[1]] == lst[param[2]] else 0
    ptr += skip[opcode-1]
    print("opcode " + str(opcode) + " skip " + str(skip[opcode-1]))
    print(" ")
