import time
import pygame


def bubblesort(screen, win_size, cell_size, arr, show):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # below code displays board to screen
                x = 0
                screen.fill((0, 0, 0))
                for element in arr:
                    pygame.draw.rect(screen, (0, 255, 0), (x, win_size - element.size[1], cell_size, element.size[1]))
                    x += cell_size + 1
                pygame.display.flip()
                if show:
                    time.sleep(.005)

    end_time = time.time() - start_time
    return arr, end_time
