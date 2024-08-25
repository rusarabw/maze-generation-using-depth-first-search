import pygame
import config
from cell import Cell

# colors
BLACK = (0, 0, 0)

# initialize pygame
pygame.init()

# set grid dimensions
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption("Maze Generation Using Depth-First Search")

stack = []

# initialize the grid
for j in range(config.rows):
    for i in range(config.cols):
        config.grid.append(Cell(i, j))


# remove walls while traversing
def remove_walls(x, y):
    dx = x.i - y.i
    if dx == 1:
        x.left_wall = False
        y.right_wall = False
    elif dx == -1:
        x.right_wall = False
        y.left_wall = False

    dy = x.j - y.j
    if dy == 1:
        x.top_wall = False
        y.bottom_wall = False
    elif dy == -1:
        x.bottom_wall = False
        y.top_wall = False


# starting point
current_cell = config.grid[0]

# driver code
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # display cells
    for cell in config.grid:
        cell.show(screen)

    # visit the starting node
    current_cell.visited = True
    current_cell.highlight(screen)

    # find a random unvisited neighbor
    next_cell = current_cell.get_neighbor()
    if next_cell:
        # visit the neighbor
        next_cell.visited = True
        # add the neighbor to the stack
        stack.append(next_cell)
        # make the path between the current cell and the next cell
        remove_walls(current_cell, next_cell)
        # move to the next cell
        current_cell = next_cell
    elif stack:
        # backtrack if there are no neighbors and the stack is not empty
        current_cell = stack.pop()

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
