import copy

arr_input = []
arr_bingos = []
arr_board = []
counter = 0
last_index_num = 0
bingo_values = [0, 0, 999]


import numpy as np

with open('aoc_2021_04_input_test.txt') as file:
    for line in file:
        if "," in line:
            arr_input.append([int(x) for x in ((line.strip().split(",")))])
        else:  
            if line != "\n": 
                arr_board.append([int(x) for x in (line.strip().split(" ")) if len(x) > 0])
                counter += 1
                if counter == 5:
                    arr_bingos.append(copy.deepcopy(arr_board))
                    arr_board.clear()
                    counter = 0
                

    for board in range(0, len(arr_bingos)):
        for line in range(0, len(arr_bingos[board])):
            for num in arr_bingos[board][line]:
                if arr_input[0].index(num) > last_index_num:
                    last_index_num = arr_input[0].index(num)
            
            if bingo_values[2] > last_index_num:
                bingo_values[0] = board
                bingo_values[1] = line
                bingo_values[2] = last_index_num

            last_index_num = 0

        board_flipped = np.transpose(arr_bingos[board]).tolist()

        for line in range(0, len(board_flipped)):
            for num in board_flipped[line]:
                if arr_input[0].index(num) > last_index_num:
                    last_index_num = arr_input[0].index(num)
            
            if bingo_values[2] > last_index_num:
                bingo_values[0] = board
                bingo_values[1] = line
                bingo_values[2] = last_index_num
                print(bingo_values)

            last_index_num = 0
    #print(np.array(arr_bingos[bingo_values[0]]).flatten().tolist())
    result_arr = np.array(arr_bingos[bingo_values[0]]).flatten().tolist()
    #print(arr_input[0][:bingo_values[2]+1])
    for number in arr_input[0][:bingo_values[2]+1]:
        if number in result_arr : result_arr.remove(number) 
    print(sum(result_arr) * arr_input[0][bingo_values[2]])
print(bingo_values)
