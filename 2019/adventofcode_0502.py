"""code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]"""
steps = [0,4,4,2,2,3,3,4,4]



def berechne_code(_code, inputvalue):
    _inputvalue = inputvalue
    arrayindex = 0

    while arrayindex < len(_code) and _code[arrayindex] != 99:

        opcode = _code[arrayindex] % 10
        print("opcode " + str(opcode))

        if _code[arrayindex] >= 100:  
            param1 = int(str(_code[arrayindex])[-3:-2])
        else:
            param1 = 0

        if _code[arrayindex] >= 1000:
            param2 = int(str(_code[arrayindex])[-4:-3])
        else:
            param2 = 0

        if _code[arrayindex] >= 10000:
            param3 = int(str(_code[arrayindex])[-5:-4])
        else:
            param3 = 0

        if opcode == 1 or opcode == 2:
            if(param1 == 0):
                value1 = _code[_code[arrayindex + 1]]
            else:
                value1 = _code[arrayindex + 1]

            if(param2 == 0):
                value2 = _code[_code[arrayindex + 2]]
            else:
                value2 = _code[arrayindex + 2]

        if(opcode == 1):
            if(param3 == 0):
                _code[_code[arrayindex + 3]] = value1 + value2
            else:
                _code[arrayindex + 3] = value1 + value2
        elif(opcode == 2):
            if(param3 == 0):
                _code[_code[arrayindex + 3]] = value1 * value2
            else:
                _code[arrayindex + 3] = value1 * value2
        elif(opcode == 3):
            print("Elif opcode == 3")
            _code[_code[arrayindex + 1]] = _inputvalue
            print(str(_code[arrayindex + 1])+ " " + str(_inputvalue))
        elif(opcode == 4):
            _inputvalue = _code[_code[arrayindex + 1]]
            print(_inputvalue)
        elif(opcode == 5):
            if param1 != 0:
                arrayindex = _code[param2]- 3
            else:
                arrayindex += steps[opcode]
        elif(opcode == 6):
            if param1 == 0:
                arrayindex = _code[param2]- 3
            else:
                arrayindex += steps[opcode]           
        elif(opcode == 7):
            if param1 < param2:
                _code[param3] = 1
            else:
                _code[param3] = 0
        elif(opcode == 8):
            if param1 == param2:
                _code[param3] = 1
            else:
                _code[param3] = 0
        else:
            print("--> Error")

        if opcode != 5 and opcode != 6:
            arrayindex += steps[opcode]

        return _code[0]


with open('./adventofcode_0502_input.txt') as file:
    for line in file:
        code = list(map(int, line.split(',')))

berechne_code(code, 1)