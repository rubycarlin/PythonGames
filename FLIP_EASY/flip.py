import pygame, random, sys
from pygame import *
from random import *
from pygame.locals import *
pygame.init()

# Variable declarations
SIZE = 300, 300
WINDOW = pygame.display.set_mode(SIZE)
WHITE = (255, 255, 255)
PINK = (255, 174, 185)
BLACK = (0, 0, 0)
mx = 0
my = 0
COLOR = PINK
COINS = 4
OFFSET = 50
START_POS = []
COLOR_MAP = []
SURFACES = []
CURLY_FONT = font.Font('LittleLordFontleroyNF.ttf', 25)
def clean():
    mx = 0
    my = 0
    for i in range(len(START_POS)):
        START_POS.pop()
    for i in range(len(COLOR_MAP)):
        COLOR_MAP.pop()
    for i in range(len(SURFACES)):
        SURFACES.pop()
        
def determine_board_size(COINS):
    width = 100 + 60 * COINS
    height = 125 + 60 * COINS
    return width, height
def define_colors(COINS):
    half = COINS * COINS / 2
    split = randint(2 , half)
    NO_OF_BLACK = split
    NO_OF_PINK = (COINS * COINS ) - split
    random_spots = []
    for i in range(split):
        x = randint(0, COINS - 1)
        y = randint(0, COINS - 1)
        random_spots.append((x, y))
    for i in range(COINS):
        colors = []
        for j in range(COINS):
            spot = i, j
            if spot in random_spots:
                colors.append(BLACK)
            else:
                colors.append(PINK)
        COLOR_MAP.append(colors)
                
def board(COINS):
    clean()
    SIZE = determine_board_size(COINS)
    WINDOW = pygame.display.set_mode(SIZE)
    WINDOW.fill(WHITE)
    row = []
    surf = []
    define_colors(COINS)
    for i in range(COINS):
        for j in range(COINS):
            x = OFFSET + j * 60
            y = OFFSET + i * 60
            row.append((x, y))
            surf.append(pygame.Surface((60, 60)))
            surf[j].fill(WHITE)
            pygame.draw.circle(surf[j], COLOR_MAP[i][j], (30, 30), 30)
            WINDOW.blit(surf[j], (x, y))
            pygame.display.update()
        START_POS.append(row)
        SURFACES.append(surf)
        row = []
        surf = []
    RESET = CURLY_FONT.render("Reset" , 1, BLACK)
    EXIT = CURLY_FONT.render("Exit", 1, BLACK)

    WINDOW.blit(RESET,(50, SIZE[1] - 50))
    WINDOW.blit(EXIT,(SIZE[0] - 70, SIZE[1] - 50)) 
    
    
def find_surface(mx, my):
    x = (my - OFFSET) / 60
    y = (mx - OFFSET) / 60
    if x < COINS and y < COINS and mx > OFFSET and my > OFFSET :
        return x, y
    else:
        return -1, -1

def find_neighbours(px, py):
    neighbours = [(px, py)]
    x , y = px, py
    while x - 1 >= 0 and y + 1 < COINS:
        neighbours.append((x - 1, y + 1))
        x = x - 1
        y = y + 1
    x , y = px, py
    while x + 1 < COINS and y - 1 >= 0:
        neighbours.append((x + 1, y - 1))
        x = x + 1
        y = y - 1
    x , y = px, py
    while y - 1 >= 0 and x - 1 >= 0:
        neighbours.append((x - 1, y - 1))
        x = x - 1
        y = y - 1
    x , y = px, py
    while y + 1 < COINS and x + 1 < COINS:
        neighbours.append((x + 1, y + 1))
        x = x + 1
        y = y + 1
    return neighbours
    
def flip(px, py):
    neighbours = find_neighbours(px, py)
    for i in range(len(neighbours)):
        x = neighbours[i][0]
        y = neighbours[i][1]
        if COLOR_MAP[x][y] == PINK:
            COLOR_MAP[x][y] = BLACK
        else:
            COLOR_MAP[x][y] = PINK             
        time.wait(100)
        pygame.draw.circle(SURFACES[x][y], COLOR_MAP[x][y], (30, 30), 30)
        WINDOW.blit(SURFACES[x][y], START_POS[x][y])
def is_game_over():
    PINK_COUNT = 0
    BLACK_COUNT = 0
    for i in range(len(COLOR_MAP)):
        PINK_COUNT += COLOR_MAP[i].count(PINK)
        BLACK_COUNT += COLOR_MAP[i].count(BLACK)
    if PINK_COUNT == 0 or BLACK_COUNT == 0:
        return True
    else:
        return False
while True:
    board(COINS)
    game = True
    while game:
        SIZE = determine_board_size(COINS)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE :
                pygame.quit()
                sys.exit
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 50 < mx < 90 and SIZE[1] - 50 < my < SIZE[1] - 30:
                    game = False
                if SIZE[0] - 70 < mx < SIZE[0] - 50 and SIZE[1] - 50 < my < SIZE[1] - 30:
                    pygame.quit()
                    sys.exit
                pos = find_surface(mx, my)
                if  pos != (-1, -1):
                    x = pos[0]
                    y = pos[1]
                    flip(x, y)
                    if(is_game_over()):
                        COINS += 1
                        game = False
        pygame.display.flip()
