import re

start = 172851
stop = 675869

pattern = r"(0{2,2})|(1{2,2})|(2{2,2})|(3{2,2})|(4{2,2})|(5{2,2})|(6{2,2})|(7{2,2})|(8{2,2})|(9{2,2})"

def count_matches(_start, _stop):
    count = 0
    for i in range(_start, _stop):
        if re.search(pattern, str(i)):
            if int(str(i)[0]) <= int(str(i)[1]) and int(str(i)[1]) <= int(str(i)[2]) and int(str(i)[2]) <= int(str(i)[3]) and int(str(i)[3]) <= int(str(i)[4]) and int(str(i)[4]) <= int(str(i)[5]):
                count += 1

    return count

print("Anzahl der Übereinstimmungen :" + str(count_matches(start,stop)))