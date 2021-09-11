import sys, pygame
pygame.init()

size = width, height = 640, 740
MINx = 20
MINy = 120
MAXx = 620
MAXy = 720
STARTx = 320
STARTy = 420



screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake by Error404')
# Initialing Color
colorPrim = (64,71,109)
colorSec = (235,101,52)
colorSnake = (100,100,100)

# Drawing Rectangle
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

checker = pygame.image.load("checker.png").convert()

while 1:
    pygame.draw.rect(screen,colorSnake,[STARTx,STARTy,10,10])
    screen.blit(checker, (0,100))
    pygame.display.flip()