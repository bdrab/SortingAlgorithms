import time
import pygame


def insertionsort(screen, win_size, cell_size, list_element, show):
    start_time = time.time()
    n = len(list_element)
    for i in range(1, n):
        key_item = list_element[i]
        j = i - 1
        while j >= 0 and list_element[j].size[1] > key_item.size[1]:
            list_element[j + 1] = list_element[j]
            j -= 1
        list_element[j + 1] = key_item

        # below code displays board to screen
        x = 0
        screen.fill((0, 0, 0))
        for element in list_element:
            pygame.draw.rect(screen, (0, 255, 0), (x, win_size - element.size[1], cell_size, element.size[1]))
            x += cell_size + 1
        pygame.display.flip()
        if show:
            time.sleep(.1)

    end_time = time.time() - start_time
    return list_element, end_time
