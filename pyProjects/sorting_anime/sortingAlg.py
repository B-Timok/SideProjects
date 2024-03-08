# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import random

# def generate_random_list(length=50, max_val=100):
#     return [random.randint(1, max_val) for _ in range(length)]

# def quicksort(A, start, end, drawing_data):
#     if start >= end:
#         return

#     pivot = A[end]
#     pivot_idx = start

#     for i in range(start, end):
#         if A[i] < pivot:
#             A[i], A[pivot_idx] = A[pivot_idx], A[i]
#             pivot_idx += 1
#         drawing_data.append(A[:])
#     A[end], A[pivot_idx] = A[pivot_idx], A[end]
#     drawing_data.append(A[:])

#     quicksort(A, start, pivot_idx-1, drawing_data)
#     quicksort(A, pivot_idx+1, end, drawing_data)

# def draw_bar(A, ax):
#     ax.clear()
#     ax.bar(range(len(A)), A)
#     plt.pause(0.1)

# def animate_quicksort(A):
#     fig, ax = plt.subplots()
#     drawing_data = [A[:]]
#     quicksort(A, 0, len(A)-1, drawing_data)
#     ani = animation.FuncAnimation(fig, draw_bar, frames=drawing_data, fargs=(ax,))
#     ani.save('quicksort_animation.gif', writer='imagemagick')  # Save the animation as a .gif file

# A = generate_random_list()
# animate_quicksort(A)

import pygame
import random

# Pygame configurations
WIDTH = 800
HEIGHT = 600
BAR_WIDTH = 5
SPACING = 7
BARS = 100
SPEED = 50

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def generate_random_list():
    return [random.randint(1, HEIGHT) for _ in range(BARS)]

def draw_bars(A, screen):
    screen.fill(WHITE)
    for i in range(len(A)):
        pygame.draw.rect(screen, BLUE, (i * SPACING, HEIGHT - A[i], BAR_WIDTH, A[i]))
    pygame.display.update()
    pygame.time.delay(SPEED)

def quicksort(A, start, end, screen):
    if start >= end:
        return

    pivot = A[end]
    pivot_idx = start

    for i in range(start, end):
        if A[i] < pivot:
            A[i], A[pivot_idx] = A[pivot_idx], A[i]
            pivot_idx += 1
        draw_bars(A, screen)
    A[end], A[pivot_idx] = A[pivot_idx], A[end]
    draw_bars(A, screen)

    quicksort(A, start, pivot_idx-1, screen)
    quicksort(A, pivot_idx+1, end, screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quicksort Visualization")
    A = generate_random_list()
    quicksort(A, 0, len(A)-1, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()