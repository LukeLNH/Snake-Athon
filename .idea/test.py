import sys, pygame
pygame.init()

size = width, height = 640, 740
MINx = 20
MINy = 120
MAXx = 620
MAXy = 720
STARTx = 320
STARTy = 420

snake_block = 10
snake_speed = 15
snake_List = []
Length_of_snake = 1
score_font = pygame.font.SysFont("comicsansms", 35)


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake by Error404')
# Initialing Color
colorPrim = (64,71,109)
colorSec = (235,101,52)
colorSnake = (100,100,100)


# Drawing Rectangle
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

checker = pygame.image.load("checker.png")

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.draw.rect(screen,colorSnake,[STARTx,STARTy,30,30])
    our_snake(snake_block, snake_List)
    screen.blit(checker, (0,100))
    pygame.display.flip()
