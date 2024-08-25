import pygame
import random
import config

# colors
WHITE = (255, 255, 255)
BLUE = (7, 1, 88)
BLACK = (0, 0, 0)


# return a cell object in the given index
def index(i, j):
    if i < 0 or j < 0 or i > config.cols-1 or j > config.rows - 1:
        return None
    return config.grid[i + j * config.cols]


class Cell:
    # constructor for a cell in the grid
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.visited = False

    # find a random unvisited neighbor of the cell (if exists)
    def get_neighbor(self):
        neighbors = []

        # get the indexes of all the neighbors
        top = index(self.i, self.j - 1)
        right = index(self.i + 1, self.j)
        bottom = index(self.i, self.j + 1)
        left = index(self.i - 1, self.j)

        # append unvisited neighbors to the list
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        # return a randomly selected neighbor(if exists) from the unvisited neighbors list
        if neighbors:
            return random.choice(neighbors)
        else:
            return None

    # highlight the cell when currently visited
    def highlight(self, screen):
        x = self.i * config.w
        y = self.j * config.w
        pygame.draw.rect(screen, BLUE, (x, y, config.w, config.w))

    # display the walls of the cell and change color if visited
    def show(self, screen):
        x = self.i * config.w
        y = self.j * config.w

        if self.visited:
            pygame.draw.rect(screen, BLACK, (x, y, config.w, config.w))

        if self.top_wall:
            pygame.draw.line(screen, WHITE, (x, y), (x + config.w, y))
        if self.right_wall:
            pygame.draw.line(screen, WHITE, (x + config.w, y), (x + config.w, y + config.w))
        if self.bottom_wall:
            pygame.draw.line(screen, WHITE, (x + config.w, y + config.w), (x, y + config.w))
        if self.left_wall:
            pygame.draw.line(screen, WHITE, (x, y + config.w), (x, y))

    def display(self):
        print(self.i, self.j, self.top_wall, self.right_wall, self.bottom_wall, self.left_wall)
