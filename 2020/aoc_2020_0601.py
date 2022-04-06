
counter = 0
questions = set()

with open('aoc_2020_06_input.txt') as file:
    for line in file:
        
        print(len(line.strip()))
        if not len(line.strip()) == 0:
            for character in line.strip():
                questions.add(character)
            print(questions)
        else:
            counter += len(questions)
            questions.clear()
            print(questions)
    counter += len(questions)   

print(counter)