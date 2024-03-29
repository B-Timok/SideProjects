# Visualization of different sorting algorithms using pygame.

import pygame
import random

# Pygame configurations
WIDTH = 700
HEIGHT = 600
BAR_WIDTH =5
SPACING = 7
BARS = 100
SPEED = 25

# Colors
BLACK = (0, 0, 0)
PINK = (255, 105, 180)

is_paused = False

def generate_random_list():
    return [random.randint(1, HEIGHT) for _ in range(BARS)]

def draw_bars(A, screen):
    global is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_paused = not is_paused
        pygame.time.wait(100)  # Wait for 100ms to reduce CPU usage
    screen.fill(BLACK)
    for i in range(len(A)):
        pygame.draw.rect(screen, PINK, (i * SPACING, HEIGHT - A[i], BAR_WIDTH, A[i]))
    pygame.display.update()
    pygame.time.delay(SPEED)

def quicksort(A, start, end, screen):
    global is_paused
    if start >= end:
        return

    pivot = A[end]
    pivot_idx = start

    for i in range(start, end):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_paused = not is_paused
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            pygame.time.wait(100)
        if A[i] < pivot:
            A[i], A[pivot_idx] = A[pivot_idx], A[i]
            pivot_idx += 1
        draw_bars(A, screen)
    A[end], A[pivot_idx] = A[pivot_idx], A[end]
    draw_bars(A, screen)

    quicksort(A, start, pivot_idx-1, screen)
    quicksort(A, pivot_idx+1, end, screen)

def bubble_sort(A, screen):
    global is_paused
    for i in range(len(A)):
        for j in range(0, len(A) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            draw_bars(A, screen)

def insertion_sort(A, screen):
    global is_paused
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        draw_bars(A, screen)

def selection_sort(A, screen):
    global is_paused
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        draw_bars(A, screen)

def merge_sort(A, screen):
    global is_paused
    if len(A) > 1:
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        merge_sort(left_half, screen)
        merge_sort(right_half, screen)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
            draw_bars(A, screen)

        while i < len(left_half):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            A[k] = left_half[i]
            i += 1
            k += 1
            draw_bars(A, screen)

        while j < len(right_half):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_paused = not is_paused
                pygame.time.wait(100)
            A[k] = right_half[j]
            j += 1
            k += 1
            draw_bars(A, screen)

def main():
    global is_paused
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("Sorting Animation")

    A = generate_random_list()
    # quicksort(A, 0, len(A)-1, screen)
    # bubble_sort(A, screen)
    # insertion_sort(A, screen)
    selection_sort(A, screen)
    # merge_sort(A, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused

if __name__ == "__main__":
    main()
