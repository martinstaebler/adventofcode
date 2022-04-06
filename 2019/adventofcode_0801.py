import numpy as np
from operator import itemgetter

image_data = []
image_layer = []
number_of_zeros = []

def count_zeros(_list):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    all_counts = []

    for item in _list: 
        if (int(item) == 0): 
            count_0 = count_0 + 1
        if (int(item) == 1): 
            count_1 = count_1 + 1
        if (int(item) == 2): 
            count_2 = count_2 + 1
    all_counts.append(count_0)
    all_counts.append(count_1)
    all_counts.append(count_2)
    return all_counts 

def decode_image(_number):
    image_data = [(_number[i:i+1]) for i in range(0, len(_number), 1)]
    image_data = np.array(image_data).reshape(100,-1)


    for i in range(0,len(image_data)):
        number_of_zeros.append(count_zeros(image_data[i]))
        image_layer.append(image_data[i].reshape(6,-1))

def find_layer(_number_of_zeros):
    list_zeros = sorted(_number_of_zeros, key=itemgetter(0))

    result = list_zeros[0][1] * list_zeros[0][2]

    return result

with open("./image_08.txt") as file:
    for line in file:
        number = line.strip()

decode_image(number)

print("Die Anzahl der Einsen und Zweien ergibt: " + str(find_layer(number_of_zeros)))