def validate_passport(fields):
    
    arr_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for i in arr_fields:
        if not i in fields:
            print("Passport invalid:", fields, "field:", i, "not found")
            return 0
    print("Passport valid:", fields)
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