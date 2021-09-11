import sys, pygame
pygame.init()

size = width, height = 640, 740
speed = [2, 2]

screen = pygame.display.set_mode(size)

# Initialing Color
colorPrim = (64,71,109)
colorSec = (235,101,52)

# Drawing Rectangle
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

checker = pygame.image.load("checker.png").convert()

ball = pygame.image.load("explosion1.gif")
ballrect = ball.get_rect()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.blit(checker, (0,100))
    screen.blit(ball, ballrect)
    pygame.display.flip()