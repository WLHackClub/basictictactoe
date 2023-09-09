
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


board = [
    ['none', 'none', 'none'],
    ['none', 'none', 'none'],
    ['none', 'none', 'none']
]
turn = 'X'


#####
# Game functions
#####


def draw_centered_text(canvas: pygame.Surface, text: pygame.Surface, x: float, y: float) -> None:
    text_rect = text.get_rect()
    canvas.blit(text, (x - text_rect.width/2, y - text_rect.height/2))


def draw_board():
    global board, canvas
    canvas.fill(0x0000aa)
    draw_centered_text(canvas, my_font.render('Tic Tac Toe', True, 0xffffffff), 600, 30)
    pygame.draw.rect(canvas, 0x000000, (495, 100, 10, 600))
    pygame.draw.rect(canvas, 0x000000, (695, 100, 10, 600))
    pygame.draw.rect(canvas, 0x000000, (300, 295, 600, 10))
    pygame.draw.rect(canvas, 0x000000, (300, 495, 600, 10))
    for x in (0, 1, 2):
        for y in (0, 1, 2):
            x_coordinate = 400 + 200*x
            y_coordinate = 200 + 200*y
            if board[y][x] == 'X':
                draw_centered_text(canvas,
                                   my_font.render('X', True, 0xff5555ff),
                                   x_coordinate, y_coordinate)
            elif board[y][x] == 'O':
                draw_centered_text(canvas,
                                   my_font.render('O', True, 0xffff55ff),
                                   x_coordinate, y_coordinate)


def mouse_button_press(pos):
    global board, turn
    x = pos[0]
    y = pos[1]
    # Check X
    if 310 <= x <= 490:
        board_x = 0
    elif 510 <= x <= 690:
        board_x = 1
    elif 710 <= x <= 890:
        board_x = 2
    else:
        # The user didn't click on the board.
        return
    # Check Y
    if 110 <= y <= 290:
        board_y = 0
    elif 310 <= y <= 490:
        board_y = 1
    elif 510 <= y <= 690:
        board_y = 2
    else:
        # The user didn't click on the board.
        return
    if board[board_y][board_x] == 'none':
        board[board_y][board_x] = turn
        turn = 'X' if turn == 'O' else 'O'


#####
# Main game
#####


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_press(event.pos)
    draw_board()
    pygame.display.update()


