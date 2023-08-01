import pygame as pg 

pg.init()
pg.display.set_caption('SUDOKU solver made by quan08')

font = pg.font.SysFont('arial', 50)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 190)
screen = pg.display.set_mode((450, 600))

sel_x = 0
sel_y = 0

board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

run = True

def draw_border(x, y, length, width=1):
    temp = x
    for column in range(3):
        for row in range(3):
            pg.draw.rect(screen, black, [x, y, length, length], width)
            x += length
        x = temp
        y += length
def game_border():
    draw_border(0, 0, 150, 2)
    _x = 0
    _y = 0
    for column in range(3):
        for row in range(3):
            draw_border(_x, _y, 50, 1)
            _x += 150
        _x = 0
        _y += 150
def print_number(board):
    alt_board = board
    x = 10
    y = -3
    for i in range(len(alt_board)):
        for j in alt_board[i]:
            if j != 0:
                num = font.render(str(j), True, black)       
            else:
                num = font.render(" ", True, black)
            screen.blit(num, (x, y))
            x += 50
        x = 10
        y += 50
def draw_button(text, x, y, width, height, bgcolor): 
    rect = pg.Rect(x, y, width, height)
    text = font.render(text, True, black)
    pg.draw.rect(screen, bgcolor, rect)
    pg.draw.rect(screen, black, rect, 2)
    text_rect = text.get_rect(center = (x + width / 2, y + height /2))
    screen.blit(text, text_rect)

def empty_location(board, l):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                l[0] = row
                l[1] = column
                return True
    return False
def used_in_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False
def used_in_column(board, column, num):
    for i in range(9):
        if board[i][column] == num:
            return True
    return False
def used_in_box(board, row, column, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + column] == num:
                return True
    return False
def check_location_is_safe(board, row, column, num):
    return (not used_in_row(board, row, num) and 
           (not used_in_column(board, column, num) and 
           (not used_in_box(board, row - row % 3, column - column % 3, num))))
def solve(board):
    l = [0, 0]
    if not empty_location(board, l):
        return True
    row = l[0]
    column = l[1]
    for num in range(1, 10):
        if check_location_is_safe(board, row, column, num):
            board[row][column] = num
            if solve(board):
                return True  
            board[row][column] = 0
    return False

while run:
    num_x = sel_x / 50
    num_y = sel_y / 50
    mouse_x, mouse_y = pg.mouse.get_pos()
    screen.fill(white)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and sel_y > 0:
                sel_y -= 50
            elif event.key == pg.K_DOWN and sel_y <= 350:
                sel_y += 50
            elif event.key == pg.K_LEFT and sel_x > 0:
                sel_x -= 50 
            elif event.key == pg.K_RIGHT and sel_x <= 350:
                sel_x += 50

            elif event.key == pg.K_1:
                board[int(num_y)][int(num_x)] = 1
            elif event.key == pg.K_2:
                board[int(num_y)][int(num_x)] = 2
            elif event.key == pg.K_3:
                board[int(num_y)][int(num_x)] = 3
            elif event.key == pg.K_4:
                board[int(num_y)][int(num_x)] = 4
            elif event.key == pg.K_5:
                board[int(num_y)][int(num_x)] = 5
            elif event.key == pg.K_6:
                board[int(num_y)][int(num_x)] = 6
            elif event.key == pg.K_7:
                board[int(num_y)][int(num_x)] = 7
            elif event.key == pg.K_8:
                board[int(num_y)][int(num_x)] = 8
            elif event.key == pg.K_9:
                board[int(num_y)][int(num_x)] = 9
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = pg.mouse.get_pressed()
            if mouse_pressed[0]:
                if 25 <= mouse_x <= 155 and 470 <= mouse_y <= 520:
                    if solve(board):
                        print('SOLVED') 
                if 25 <= mouse_x <= 155 and 530 <= mouse_y <= 580:
                    board = [
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            ]
    game_border()
    print_number(board)
    pg.draw.rect(screen, green, [sel_x, sel_y, 50, 50], 3)
    draw_button('Solve', 25, 470, 130, 50, green)
    draw_button('Reset', 25, 530, 130, 50 , blue)
    pg.display.update()