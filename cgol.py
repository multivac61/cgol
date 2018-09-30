# Copyright 2013, Olafur Bogason
# Conway's game of life.
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# The console print is based of
# http://code.activestate.com/recipes/578167-position-the-cursor-almost-anywhere-inside-standar/
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# This is a bare-bone alpha version merely coded to make a sort-of skeleton for future versions. 
# Future versions will most definitely have OOP and a nicer console display (maybe colour! who knows).

# v.02 30/09/18 - OOP Implemented. Nicer console display remains missing..


from time import sleep
import numpy as np
from os import system, name


class GameOfLife:
    Offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    def __init__(self, n, m):
        self.N, self.M = n, m
        self.current_grid, self.future_grid = np.zeros((n, m)), np.zeros((n, m))

    def evolve(self):
        """
        Evolve current grid as dictated by the rule of Life
        """
        for row in range(self.N):
            for col in range(self.M):
                self.evolve_cell(row, col)

        self.current_grid = np.copy(self.future_grid)

    def randomize(self, chance):
        """
        Randomly populate the current grid with a given chance
        :param chance: How likely it is for each cell to spring to life
        """
        self.current_grid = np.vectorize(lambda x: 1 if x > chance else 0)(np.random.rand(self.N, self.M))

    def neighbours(self, i, j):
        """
        Returns how many alive neighbours the cell at point (i, j) has.
        :param i: i-th row
        :param j: j-th column
        :return: number of alive neighbours to cell (i, j)
        """
        alive_neighbours = 0
        for (ii, jj) in self.Offsets:
            x, y = i + ii, j + jj
            if 0 <= x < self.N and 0 <= y < self.M and self.current_grid[x, y] == 1:
                alive_neighbours += 1

        return alive_neighbours

    def evolve_cell(self, i, j):
        """
        Evolve the cell at (i, j) at future grid
        :param i: i-th row
        :param j: j-th column
        """
        alive = (self.current_grid[i, j] == 1)
        neighbours = self.neighbours(i, j)

        if alive:
            next_state = not (neighbours < 2 or neighbours > 3)
        else:
            next_state = (neighbours == 3)

        self.future_grid[i, j] = next_state


def clear_console():
    """
    Clear the Python console.
    """
    system('cls' if name == 'nt' else 'clear')


def query_user():
    """
    Ask user for size of squared life, the chance of initial life and the timestep to delay
    :return: grid size, chance of life [0, 1[ and time delay between evolutions
    """
    print """Oh holy ruler, welcome to \n
        #####  #####  #####  ##   [v.02]
        ##     ##     ##  #  ##
        ##     ## ##  ##  #  ##
        #####  #####  #####  ######"""

    grid_size = int(raw_input('Please input the size of The Garden of Eden [positive integer]: '))
    chance_of_life = float(raw_input('Please input the chances of initial life [positive double between 0-1 ]: '))
    evolve_timestep = float(
        raw_input('Please specify the time period which life should develop by [positive double]: '))

    return grid_size, chance_of_life, evolve_timestep


if __name__ == "__main__":
    size, my_chance, timestep = query_user()

    gol = GameOfLife(size, size)
    gol.randomize(my_chance)

    # # Glider
    # gol.current_grid[0, 1] = 1
    # gol.current_grid[1, 2] = 1
    # gol.current_grid[2, 0] = 1
    # gol.current_grid[2, 1] = 1
    # gol.current_grid[2, 2] = 1

    while True:
        print gol.current_grid

        gol.evolve()

        sleep(timestep)
        clear_console()
