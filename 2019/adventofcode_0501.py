code = []
steps = [0,4,4,2,2,3,3,4,4]

def berechne_code(_code, inputvalue):
    _inputvalue = inputvalue
    arrayindex = 0
    

    while arrayindex < len(_code) and _code[arrayindex] != 99:

        opcode = int(str(_code[arrayindex])[-1:])
        print("opcode " + str(_code[arrayindex]))

        if(_code[arrayindex] >= 100):        
            param1 = int(str(_code[arrayindex])[-3:-2])
        else:
            param1 = 0

        if(_code[arrayindex] >= 1000):
            param2 = int(str(_code[arrayindex])[-4:-3])
        else:
            param2 = 0

        if(_code[arrayindex] >= 10000):
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
            _code[_code[arrayindex + 1]] = _inputvalue
        elif(opcode == 4):
            _inputvalue = _code[_code[arrayindex + 1]]
            print(_inputvalue)
        else:
            print("--> Error")

        arrayindex += steps[opcode]

    return _code[0]

with open('./air_conditioner_05.txt') as file:
    for line in file:
        code = list(map(int, line.split(',')))

berechne_code(code, 1)