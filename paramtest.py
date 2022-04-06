testcode = 123456789

opcode = int(str(testcode)[-2:])
param1 = int(str(testcode)[-3:-2])
print("opcode: " + str(testcode) + " " + str(param1))