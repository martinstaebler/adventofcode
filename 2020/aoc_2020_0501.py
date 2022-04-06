
import numpy as np

seats = np.empty([128,8])
seats.fill(0)


highest_id = 0
id = 0

with open('aoc_2020_05_input.txt') as f:
    for line in f:
        row = 0
        column = 0
        rows = 128
        columns = 8
        string_row = line.strip()[0:7]
        string_column = line.strip()[7:10]
        for i in string_row:
            rows = int(rows / 2)
            if i == "F":
                pass
            else:
                row += rows 

        for i in string_column:
            columns = int(columns / 2)
            if i == "L":
                pass
            else:
                column += columns
        seats[row][column] = 1
        id = row * 8 + column
        #print(row, column, id)
        if id > highest_id:
            highest_id = id
            
        
    print("highest ID", highest_id)
    for i in range(3, 124):
        for j in range(0, 8):
            if seats[i][j] == 0:
                id = i * 8 + j
                print("empty", i, j, id)

        

    
