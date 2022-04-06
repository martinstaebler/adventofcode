code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]

def berechne_code(input):
    input_code = input.copy
 
    for i in range(1, 100):
        for r in range(1, 100):
            arrayindex = 0
            input_code = input.copy()
            input_code[1] = i
            input_code[2] = r

            while arrayindex < len(input_code) and input_code[arrayindex] != 99:
                
                if(input_code[arrayindex]) == 1:
                    input_code[input_code[arrayindex + 3]] = input_code[input_code[arrayindex + 1]] + input_code[input_code[arrayindex + 2]]
                elif(input_code[arrayindex]) == 2:
                    input_code[input_code[arrayindex + 3]] = input_code[input_code[arrayindex + 1]] * input_code[input_code[arrayindex + 2]]
                else:
                    print("Error")
                
                if(input_code[arrayindex]) == 99:
                    break
                else:
                    arrayindex += 4
            if(input_code[0] >= 19690720):
                break
        if(input_code[0] >= 19690720):
            break
    return str(i) + " "  + str(r) + " " + str(input_code[0])

print("Ergebnis: " + str(berechne_code(code)))