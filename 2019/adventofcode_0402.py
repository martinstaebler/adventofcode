import re

start = 172851
stop = 675869

pattern1 = r"(0{2,2})|(1{2,2})|(2{2,2})|(3{2,2})|(4{2,2})|(5{2,2})|(6{2,2})|(7{2,2})|(8{2,2})|(9{2,2})"
pattern2 =  r"(0{3,5})|(1{3,5})|(2{3,5})|(3{3,5})|(4{3,5})|(5{3,5})|(6{3,5})|(7{3,5})|(8{3,5})|(9{3,5})"

def count_matches(_start, _stop):
    count = 0
    for i in range(_start, _stop):
        if re.search(pattern1, str(i)):
            if int(str(i)[0]) <= int(str(i)[1]) and int(str(i)[1]) <= int(str(i)[2]) and int(str(i)[2]) <= int(str(i)[3]) and int(str(i)[3]) <= int(str(i)[4]) and int(str(i)[4]) <= int(str(i)[5]):
                if re.search(pattern2, str(i)):
                    numbers = re.sub(pattern2,'',str(i))
                    if re.search(pattern1, numbers):
                        count += 1
                else:
                    count += 1

    return count

print("Anzahl der Übereinstimmungen :" + str(count_matches(start,stop)))