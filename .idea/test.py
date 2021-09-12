import sys, pygame
pygame.init()

size = width, height = 640, 740

#limits for snake movement
MINx = 20
MINy = 120
MAXx = 620
MAXy = 720

#start for snake
STARTx = 320
STARTy = 420

Length_of_snake = 1

score_font = pygame.font.SysFont("timesnewroman", 35)
#function that sets score
def Your_score(score):
    value = score_font.render("Current Score: " + str(score), True, colorSec)
    screen.blit(value, [50, 50])


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake by Error404')

# Initialing Color
colorPrim = (64,71,109)
colorSec = (130,103,84)
colorSnake = (66,158,94)

# Drawing Rectangle/Background
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

#load checker
checker = pygame.image.load("checker.png")
screen.blit(checker, (0,100))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    Your_score(Length_of_snake - 1)
    #increase length when eat, call your score

    #creates snake rect and updates screen 2nd line
    pygame.draw.rect(screen,colorSnake,[STARTx,STARTy,30,30])
    pygame.display.flip()
