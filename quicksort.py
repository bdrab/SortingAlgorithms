import random
import time
import pygame


def quicksort(list_to_sort, screen=None, win_size=None, cell_size=None, show=None):

    if len(list_to_sort) < 2:
        return list_to_sort

    smaller = []
    same_as_random = []
    bigger = []

    random_element = random.choice(list_to_sort).size[1]
    for element in list_to_sort:
        if element.size[1] > random_element:
            bigger.append(element)
        elif element.size[1] < random_element:
            smaller.append(element)
        else:
            same_as_random.append(element)

    return quicksort(smaller) + same_as_random + quicksort(bigger)


def quicksort_algorithm(list_to_sort, screen=None, win_size=None, cell_size=None, show=None):
    x = 0
    start_time = time.time()
    screen.fill((0, 0, 0))
    sorted_list = quicksort(list_to_sort)
    for element in sorted_list:
        pygame.draw.rect(screen, (0, 255, 0), (x, win_size - element.size[1], cell_size, element.size[1]))
        x += cell_size + 1
    pygame.display.flip()
    end_time = time.time() - start_time

    return sorted_list, end_time

