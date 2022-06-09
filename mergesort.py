import time
import pygame


def merge(list_1, list_2):
    if len(list_1) == 0:
        return list_2
    if len(list_2) == 0:
        return list_1

    result_list = []
    list_1_index = 0
    list_2_index = 0
    print("list_1", list_1)
    print("list_2", list_2)

    while len(result_list) < (len(list_1) + len(list_2)):

        if list_1[list_1_index] <= list_2[list_2_index]:
            result_list.append(list_1[list_1_index])
            list_1_index += 1
        else:
            result_list.append(list_2[list_2_index])
            list_2_index += 1

        if len(list_1) == list_1_index:
            result_list += list_2[list_2_index:]
            break
        if len(list_2) == list_2_index:
            result_list += list_1[list_1_index:]
            break
    print("resultlist", result_list)
    return result_list


#def mergesort(screen, win_size, cell_size, arr, show):
def mergesort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    midpoint = len(list_to_sort) // 2

    return merge(list_1=mergesort(list_to_sort[:midpoint]), list_2=mergesort(list_to_sort[midpoint:]))

print(mergesort([1, 3, 8, 2, 4, 6]))
