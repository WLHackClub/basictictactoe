
import pygame


#####
# Initialize pygame
#####

pygame.init()
pygame.display.set_caption("Tic Tac Toe by greateric")
pygame_canvas = pygame.display.set_mode((1200, 800))

# "Times New Roman", "Courier New", "Ubuntu Mono", etc.
my_font = pygame.font.SysFont('Calibri', 36)


#####
# Game functions
#####


def draw_centered_text(canvas: pygame.Surface, text: pygame.Surface, x: float, y: float) -> None:
    text_rect = text.get_rect()
    canvas.blit(text, (x - text_rect.width/2, y - text_rect.height/2))


def draw_board(canvas):
    canvas.fill(0x00aaaa)
    draw_centered_text(canvas, my_font.render('Tic Tac Toe', True, 0xffffffff), 600, 50)


#####
# Main game loop
#####

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # TODO: What if the user clicks on the screen?
    draw_board(pygame_canvas)
    pygame.display.update()


