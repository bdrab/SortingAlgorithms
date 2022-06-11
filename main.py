import random
import time
import pygame
from bubblesort import bubblesort_algorithm
from mergesort import mergesort_algorithm
from quicksort import quicksort_algorithm
from timesort import timesort_algorithm
from insertionsort import insertionsort_algorithm


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIN_SIZE = 500
CELL_SIZE = 10
ROWS = WIN_SIZE // CELL_SIZE

functions = {0: bubblesort_algorithm,
             1: mergesort_algorithm,
             2: quicksort_algorithm,
             3: timesort_algorithm,
             4: insertionsort_algorithm}

algorithms_name = ["Bubble Sort", "Merge Sort", "Quick Sort", "Time Sort", "Insertion Sort"]
algorithms_number = len(algorithms_name)


def shuffle_elements():
    random.shuffle(heights)
    del elements[:]
    for z, height in enumerate(heights):
        rect = pygame.draw.rect(screen, (255, 0, 0), (z * CELL_SIZE, WIN_SIZE - height, CELL_SIZE, height))
        elements.append(rect)


pygame.init()
screen = pygame.display.set_mode((WIN_SIZE+50, WIN_SIZE))
pygame.display.set_caption("Sorting Algorithms")
font = pygame.font.Font(None, 40)


heights = [h for h in range(0, WIN_SIZE, WIN_SIZE // ROWS)]
random.shuffle(heights)
elements = []
end_program = False

while not end_program:
    mode_set = False
    number = 0
    shuffle_elements()

    while not mode_set:
        algorithms = []
        for i, name in zip(range(algorithms_number), algorithms_name):
            if i < 1:
                algorithm = pygame.draw.rect(screen, WHITE, (0, 0, screen.get_width(), WIN_SIZE / algorithms_number))
            else:
                algorithm = pygame.draw.rect(screen, WHITE, (0, algorithms[-1].bottom, screen.get_width(),
                                                             WIN_SIZE / algorithms_number))

            algorithm_text = font.render(f"{name} algorithm ", True, (0, 0, 0))
            algorithm_text_rect = algorithm_text.get_rect(center=(algorithm.centerx, algorithm.centery))
            screen.blit(algorithm_text, algorithm_text_rect)
            algorithms.append(algorithm)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                end_program = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()[1]
                    number = int(pos // (WIN_SIZE/5))
                    mode_set = True
        pygame.display.flip()

    sorted_list, time_ex = functions[number](elements, screen, WIN_SIZE, CELL_SIZE, True)
    print(f"Time needed to sort the list: {time_ex} ")
    time.sleep(1)
