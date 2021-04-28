import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920,1080
size = (width, height)
#size of the screen

pygame.init()
pygame.display.set_caption("Jeu de la vie (verre d'eau)")
#the name of our game/window
screen = pygame.display.set_mode(size)
#size of the game screen
clock = pygame.time.Clock()
fps = 30
#making it 30 frame per second to see it clear


#a lot of colors to change between them depending on themes
#for now i am using sparkling water glass theme

#black = (0, 0, 0)
#blue = (0, 119, 190)
#turquoise = (48,213,200)
#red = (220,20,60)
#thuderYellow = (255,255,0)
#white = (255, 255, 255)
bubbles = (231,254,255)
water = (131,215,238)

scaler = 40
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()


run = True
while run:
    clock.tick(fps)
    #speed of the game 
    screen.fill(water)
    #background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    Grid.Conway(off_color=water, on_color=bubbles, surface=screen)
    #off_color is the basic grid color
    #on_color is the infected case/pixel
    #surface is the whole background
    pygame.display.update()
    #update with time it is not static

pygame.quit()