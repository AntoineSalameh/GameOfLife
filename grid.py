import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        #scale will be defined in main

        self.columns = int(height/scale)
        self.rows = int(width/scale)
        #size will be defined in main (height and width)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
                #to see if the cell has been infected or no 
                #if 1 the cell is infected 
                #if 0 the cell is clear


    def Conway(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    #if cell infected
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    #cell is clear

        next = np.ndarray(shape=(self.size))
        #that is to infect other cells or clear a cell
        #depending on it state and neighbour cells
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours( x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next


    #here will be for the cells next to the infected cell 
    #we count the numbers of cells around it and if it is also infected or not
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total