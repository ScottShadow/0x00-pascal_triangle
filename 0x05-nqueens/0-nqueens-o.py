#!/usr/bin/python3
import copy
board_size = 5


def Queens(n):
    my_list = [[0, 0]]
    listoflists = []
    step = 2
    level = 1
    status = True
    key_list = []
    for _ in range(n):
        print("\n--------\n")
        while my_list[len(my_list)-1][0] < (n-1):
            if level >= (n/2):
                level = 0
                step -= 1
            checkNode(n, my_list, step, level)
            level += 1
            step = 2
        for key in my_list:
            key_list.append(key[1])
        print(f"key_list = {key_list}")
        for k in range(len(key_list)-1):
            if key_list[k] - key_list[k+1] == 1 or key_list[k+1] - key_list[k] == 1:
                print(f"{key_list[k]} - {key_list[k+1]} < 2")
                status = False
                break

        if status:
            listoflists.append(my_list)
            key_list.reverse()
            print(f"reversed key_list = {key_list}")
            original_list = copy.deepcopy(my_list)
            for k in range(len(key_list)):
                original_list[k][1] = key_list[k]
            listoflists.append(original_list)
        print("BIG LIST -:> ")
        for k in listoflists:
            print(k)
        my_list = [[my_list[0][0], my_list[0][1]]]
        my_list[0][1] += 1
        level = 1
        status = True
        key_list = []


def checkNode(n, my_list, step, level):
    i = len(my_list) - 1
    print(f"i:{i}, step: {step}, level: {level}")
    print(f"my_list : {my_list[i][1]}")
    mod = n
    my_list.append([my_list[i][0]+1, (my_list[i][1]+(level*n)+step) % mod])
    step = 2
    print(my_list)


Queens(5)
