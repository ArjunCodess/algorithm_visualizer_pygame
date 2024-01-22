import pygame
import random
import math

pygame.init()


# The `DrawInformation` class is used for storing and managing information related to drawing elements
# on a window.
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 128, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (0, 0, 255),
        (0, 0, 230),
        (0, 0, 205),
    ]

    SMALL_FONT = pygame.font.SysFont("timesnewroman", 15)
    FONT = pygame.font.SysFont("timesnewroman", 20)
    LARGE_FONT = pygame.font.SysFont("timesnewroman", 30)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("SortingWiz")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val)
        )
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    """
    The `draw` function is responsible for rendering the sorting visualization on the screen, including
    the title, controls, sorting options, the list being sorted, and additional information.

    :param draw_info: The `draw_info` parameter is an object that contains information about the drawing
    window and other drawing-related properties. It likely includes attributes such as `window` (the
    drawing window), `BACKGROUND_COLOR` (the background color of the window), `LARGE_FONT` (a large font
    for titles),
    :param algo_name: The `algo_name` parameter is a string that represents the name of the sorting
    algorithm being used. It will be displayed in the title of the window
    :param ascending: The `ascending` parameter is a boolean value that determines whether the sorting
    algorithm should sort the data in ascending order (`True`) or descending order (`False`)
    :param time_complexity: The time complexity of the current algorithm.
    :param space_complexity: The space complexity of the current algorithm.
    """

    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title_text = f"{algo_name} - {'Ascending' if ascending else 'Descending'}"
    title_font = draw_info.LARGE_FONT
    title_surface = title_font.render(title_text, 1, draw_info.GREEN)

    # Calculate the position with padding
    title_x = draw_info.width / 2 - title_surface.get_width() / 2
    title_y = -30  # Padding before the title
    title_y += title_surface.get_height() + 0  # Padding after the title

    draw_info.window.blit(title_surface, (title_x, title_y))

    controls_text = "Q - Quit | R - Reset | SPACE - Start/Resume/Stop | A - Ascending | D - Descending"
    controls_font = draw_info.FONT
    controls_surface = controls_font.render(controls_text, 1, draw_info.BLACK)
    controls_x = draw_info.width / 2 - controls_surface.get_width() / 2
    controls_y = title_y + title_surface.get_height()
    draw_info.window.blit(controls_surface, (controls_x, controls_y))

    sorting_text = (
        "I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Heap Sort"
    )
    sorting_surface = draw_info.FONT.render(sorting_text, 1, draw_info.BLACK)
    sorting_x = draw_info.width / 2 - sorting_surface.get_width() / 2
    sorting_y = controls_y + controls_surface.get_height()
    draw_info.window.blit(sorting_surface, (sorting_x, sorting_y))

    # Display time and space complexity based on the selected algorithm
    if algo_name == "Bubble Sort":
        time_complexity = "O(n^2)"
        space_complexity = "O(1)"
    elif algo_name == "Insertion Sort":
        time_complexity = "O(n^2)"
        space_complexity = "O(1)"
    elif algo_name == "Selection Sort":
        time_complexity = "O(n^2)"
        space_complexity = "O(1)"
    elif algo_name == "Heap Sort":
        time_complexity = "O(n log n)"
        space_complexity = "O(1)"
    else:
        time_complexity = "Not specified"
        space_complexity = "Not specified"

    complexity_text = (
        f"Time Complexity: {time_complexity} | Space Complexity: {space_complexity}"
    )
    complexity_surface = draw_info.SMALL_FONT.render(
        complexity_text, 1, draw_info.BLACK
    )
    complexity_x = draw_info.width / 2 - complexity_surface.get_width() / 2
    complexity_y = sorting_y + sorting_surface.get_height() + 10  # Padding on top
    draw_info.window.blit(complexity_surface, (complexity_x, complexity_y))

    draw_list(draw_info)

    # Additional information
    additional_info_text = "[CS50 Fall 2023 Final Project - SortingWiz | Made by Arjun Vijay Prakash (@ArjunCodess)]"
    additional_info_surface = draw_info.SMALL_FONT.render(
        additional_info_text, 1, draw_info.BLACK
    )
    additional_info_x = draw_info.width / 2 - additional_info_surface.get_width() / 2
    additional_info_y = (
        complexity_y + complexity_surface.get_height() + 5
    )  # Padding on bottom
    draw_info.window.blit(
        additional_info_surface, (additional_info_x, additional_info_y)
    )

    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    """
    The function `draw_list` takes in a list of values and draws rectangles on a window based on the
    values in the list.

    :param draw_info: The `draw_info` parameter is an object that contains information needed to draw
    the list. It likely has the following attributes:
    :param color_positions: The `color_positions` parameter is a dictionary that specifies the positions
    in the list where you want to change the color of the blocks. The keys of the dictionary represent
    the positions in the list, and the values represent the color you want to assign to those positions
    :param clear_bg: The `clear_bg` parameter is a boolean value that determines whether the background
    of the drawing window should be cleared before drawing the list. If `clear_bg` is `True`, a
    rectangle covering the entire drawing window will be filled with the background color specified in
    `draw_info.BACKGROUND_COLOR`. If, defaults to False (optional)
    """
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD // 2,
            draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD,
            draw_info.height - draw_info.TOP_PAD,
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(
            draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)
        )

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    """
    The function generates a list of random integers within a given range.

    :param n: The parameter "n" represents the number of elements you want in the list
    :param min_val: The minimum value that can be generated in the list
    :param max_val: The maximum value that can be generated in the list
    :return: a list of n random integers between min_val and max_val.
    """
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_idx] and ascending) or (
                lst[j] > lst[min_idx] and not ascending
            ):
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

    return lst


def heapify(draw_info, lst, n, i, ascending):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (
        (lst[left] > lst[largest] and ascending)
        or (lst[left] < lst[largest] and not ascending)
    ):
        largest = left

    if right < n and (
        (lst[right] > lst[largest] and ascending)
        or (lst[right] < lst[largest] and not ascending)
    ):
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)
        yield True

        yield from heapify(draw_info, lst, n, largest, ascending)


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, lst, n, i, ascending)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
        yield True

        yield from heapify(draw_info, lst, i, 0, ascending)

    return lst


def main():
    """
    The main function controls the sorting visualization program, allowing the user to select different
    sorting algorithms and sort the list in ascending or descending order.
    """
    run = True
    clock = pygame.time.Clock()

    n = 100
    min_val = 0
    max_val = 200

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1200, 1000, lst)
    sorting = False
    ascending = True
    step_by_step = False
    sorting_paused = False

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting and not sorting_paused:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(
                        draw_info, ascending
                    )
                elif event.key == pygame.K_RETURN and not sorting:
                    sorting_paused = False
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                elif event.key == pygame.K_h and not sorting:
                    sorting_algorithm = heap_sort
                    sorting_algo_name = "Heap Sort"
                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                elif event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_SPACE and sorting and not sorting_paused:
                    sorting_paused = True
                elif event.key == pygame.K_SPACE and sorting and sorting_paused:
                    sorting_paused = False

    pygame.quit()


if __name__ == "__main__":
    main()
