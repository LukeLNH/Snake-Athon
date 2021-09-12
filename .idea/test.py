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
snake_List = [1,2,3,4]
Length_of_snake = 1
score_font = pygame.font.SysFont("comicsansms", 35)


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake by Error404')
# Initialing Color
colorPrim = (64,71,109)
colorSec = (235,101,52)
colorSnake = (66,158,94)

# Drawing Rectangle
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

checker = pygame.image.load("checker.png")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(checker, (0,100))
    pygame.draw.rect(screen,colorSnake,[STARTx,STARTy,30,30])
    pygame.display.flip()
