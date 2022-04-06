import re

def validate_passport(fields):

    dict_values = {}
    arr_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    eye_colors = ["amb","blu","brn","gry","grn","hzl","oth"]

    arr_values = re.split('[ \\s]+', fields.strip())
    for i in arr_values:
        key_and_value = i.split(":")
        dict_values[key_and_value[0]] = key_and_value[1]

    for i in arr_fields:
        if not i in fields:
            print("Passport invalid:", fields, "field:", i, "not found")
            return 0
        else:
            if i == "byr":
                if not (1920 <= int(dict_values[i]) <= 2002):
                    print(dict_values[i],"byr invalid")
                    return 0 

            if i == "iyr":
                if not (2010 <= int(dict_values[i]) <= 2020):
                    print(dict_values[i],"iyr invalid")
                    return 0

            if i == "eyr":
                if not (2020 <= int(dict_values[i]) <= 2030):
                    print(dict_values[i], "eyr invalid")
                    return 0

            if i == "hgt":
                string_split = re.split('(\d+)',dict_values[i])
                if not len(string_split[2]) >= 2:
                    print(dict_values[i], string_split[0], "hgt1 invalid")
                    return 0
                else:
                    if (150 <= int(string_split[1]) <= 193 and string_split[2] == "cm") or (59 <= int(string_split[1]) <= 76 and string_split[2] == "in"):
                        print(dict_values[i], string_split[0], "hgt")
                        pass
                    else:
                        print("hgt2 invalid", dict_values[i])
                        return 0

            if i == "hcl":
                if re.match("#[0-9,a-z]{6}", dict_values[i]) == None:
                    print("hcl invalid", dict_values[i])
                    return 0

            
            if i == "ecl":
                if any(x in dict_values[i] for x in eye_colors) == False:
                    print(dict_values[i],"ecl invalid")
                    return 0
                else:
                    print(dict_values[i],"ecl")
            
            if i == "pid":
                #print(re.match("[0-9]{9}", dict_values[i]))
                if re.match("^[0-9]{9}$", dict_values[i]) == None:
                    print("pid invalid", dict_values[i])
                    return 0
                else:
                    print("pid", dict_values[i])
  
    #print("Passport valid:", fields)
    return 1



passport = ""
counter = 0

with open('aoc_2020_04_input.txt') as f:
    for line in f:
        #print(len(line))
        if not len(line) == 1:
            passport += (line.strip() + " ")
            #print(passport)
        elif len(line) == 1:
            counter += validate_passport(passport)
            passport = ""
    counter += validate_passport(passport)    


print(f'valid passports: {counter}')   