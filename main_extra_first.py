
import pygame


#####
# Initialize pygame
#####


pygame.init()
pygame.display.set_caption("Tic Tac Toe by greateric")
canvas = pygame.display.set_mode((1200, 800))

# "Times New Roman", "Courier New", "Ubuntu Mono", etc.
my_font = pygame.font.SysFont('Calibri', 36)


#####
# Game state
#####


#####
# Game functions
#####


def draw_centered_text(canvas: pygame.Surface, text: pygame.Surface, x: float, y: float) -> None:
    text_rect = text.get_rect()
    canvas.blit(text, (x - text_rect.width/2, y - text_rect.height/2))


def draw_board():
    global canvas
    canvas.fill(0x0000aa)
    draw_centered_text(canvas, my_font.render('Tic Tac Toe', True, 0xffffffff), 600, 30)
    pygame.draw.rect(canvas, 0x000000, (495, 100, 10, 600))
    pygame.draw.rect(canvas, 0x000000, (695, 100, 10, 600))
    pygame.draw.rect(canvas, 0x000000, (300, 295, 600, 10))
    pygame.draw.rect(canvas, 0x000000, (300, 495, 600, 10))


#####
# Main game
#####


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_board()
    pygame.display.update()


