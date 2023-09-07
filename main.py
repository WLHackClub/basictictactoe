
import pygame


#####
# Initialize pygame
#####

pygame.init()
pygame.display.set_caption("Tic Tac Toe by greateric")
canvas = pygame.display.set_mode((1200, 800))


#####
# Game functions
#####


def draw_board(c):
    c.fill(0x00aaaa)


#####
# Main game loop
#####

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # TODO: What if the user clicks on the screen?
    draw_board(canvas)
    pygame.display.update()


