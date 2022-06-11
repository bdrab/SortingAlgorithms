import time
import pygame


def insertionsort_algorithm(list_to_sort, screen=None, win_size=None, cell_size=None, show=None):
    start_time = time.time()
    n = len(list_to_sort)
    for i in range(1, n):
        key_item = list_to_sort[i]
        j = i - 1
        while j >= 0 and list_to_sort[j].size[1] > key_item.size[1]:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        list_to_sort[j + 1] = key_item

        # below code displays board to screen
        x = 0
        screen.fill((0, 0, 0))
        for element in list_to_sort:
            pygame.draw.rect(screen, (0, 255, 0), (x, win_size - element.size[1], cell_size, element.size[1]))
            x += cell_size + 1
        pygame.display.flip()
        if show:
            time.sleep(.1)

    end_time = time.time() - start_time
    return list_to_sort, end_time
