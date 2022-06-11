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

    while len(result_list) < (len(list_1) + len(list_2)):

        if list_1[list_1_index].size[1] <= list_2[list_2_index].size[1]:
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

    return result_list


def mergesort(list_to_sort):

    if len(list_to_sort) <= 1:
        return list_to_sort
    midpoint = len(list_to_sort) // 2

    return merge(list_1=mergesort(list_to_sort[:midpoint]), list_2=mergesort(list_to_sort[midpoint:]))


def mergesort_algorithm(list_to_sort, screen=None, win_size=None, cell_size=None, show=None):
    x = 0
    start_time = time.time()
    screen.fill((0, 0, 0))
    sorted_list = mergesort(list_to_sort)
    for element in sorted_list:
        pygame.draw.rect(screen, (0, 255, 0), (x, win_size - element.size[1], cell_size, element.size[1]))
        x += cell_size + 1
    pygame.display.flip()
    end_time = time.time() - start_time

    return sorted_list, end_time
