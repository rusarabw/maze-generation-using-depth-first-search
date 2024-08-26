
# Maze Generation Using Depth-First Search

Maze should be a grid of 20 rows by 20 columns. DFS algorithm is used to generate the maze. 


## How it Works?

* Initialize a grid with cells each having walls in all four directions.
* Start from the starting cell and randomly select an unvisited neighbor.
* Visit the unvisited neighbor while removing the wall between the current node and the neighbor.
* Push the neighbor into a stack.
* Iterate the process until there are no unvisited neighbors.
* If there are no unvisited neighbors, pop the stack and set the popped cell as the current cell.
* Iterate this entire process until the stack is empty.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/). From your command line:

```bash
# Clone this repository
$ git clone https://github.com/rusarabw/maze-generation-using-depth-first-search.git

# Go into the repository
$ cd maze-generation-using-depth-first-search

# Install libraries
$ pip install pygame

# Run the program
$ python main.py

```

## Generated Maze

![Generated Maze](https://github.com/rusarabw/maze-generation-using-depth-first-search/blob/master/screenshot.jpeg?raw=true)



