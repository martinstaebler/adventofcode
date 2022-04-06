code = []
steps = [0,4,4,2,2,3,3,4,4]

def berechne_code(_code, inputvalue):
    _inputvalue = inputvalue
    arrayindex = 0
    print(f'_code {_code}')

    while arrayindex < len(_code) and _code[arrayindex] != 99:
        #weiter = input('Weiter?: ')
        opcode = int(str(_code[arrayindex])[-1:])
        

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

        print("opcode " + str(_code[arrayindex]) + " arrayindex: " + str(arrayindex) + " params: " + str(param3) + "" + str(param2) + "" + str(param1))

        if opcode == 1 or opcode == 2:
            if(param1 == 0):
                value1 = _code[_code[arrayindex + 1]]
            else:
                value1 = _code[arrayindex + 1]

            if(param2 == 0):
                value2 = _code[_code[arrayindex + 2]]
            else:
                value2 = _code[arrayindex + 2]

        if opcode == 1:
            if param3 == 0:
                _code[_code[arrayindex + 3]] = value1 + value2
            else:
                _code[arrayindex + 3] = value1 + value2
        elif opcode == 2:
            if param3 == 0:
                _code[_code[arrayindex + 3]] = value1 * value2
            else:
                _code[arrayindex + 3] = value1 * value2
        elif opcode == 3:
            _code[_code[arrayindex + 1]] = _inputvalue

        elif opcode == 4:
            _inputvalue = _code[_code[arrayindex + 1]]
            print(f'_inputvalue {_inputvalue}')

        elif opcode == 5 and param1 != 0 or opcode == 6 and param1 == 0:
            print("param2 " + str(param2) + " " + str(_code[param2]))
            arrayindex += 2 - steps[opcode]
          
        elif opcode == 7:
            if _code[_code[arrayindex + 1]] < _code[_code[arrayindex + 2]]:
                _code[_code[arrayindex + 3]] = 1
            else:
                _code[_code[arrayindex + 3]] = 0
        elif opcode == 8:
            if _code[_code[arrayindex + 1]] == _code[_code[arrayindex + 2]]:
                _code[_code[arrayindex + 3]] = 1
            else:
                _code[_code[arrayindex + 3]] = 0

        elif opcode == 0:
            exit

        else:
            print("--> Error")

        arrayindex += steps[opcode]

        print(f'_code {_code}')

    if opcode == 0:
        exit

    return _code[0]

with open('./adventofcode_0502_input.txt') as file:
    for line in file:
        code = list(map(int, line.split(',')))

print(berechne_code(code, 1))