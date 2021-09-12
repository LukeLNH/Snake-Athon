import pygame
import random
import sys
pygame.init()

screen_width = 640
screen_height = 640
grid_size = 30

# Initialing Color
colorPrim = (64,71,109)
colorSec = (130,103,84)
colorSnake = (66,158,94)

size = width, height = 640, 640 #740
MINx = 20
MINy = 120
MAXx = 620
MAXy = 720
STARTx = 320
STARTy = 420

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake by Error404')
score_font = pygame.font.SysFont("timesnewroman", 35)

# Drawing Rectangle
pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))
#load checker
checker = pygame.image.load("checker.png")

#function that sets score
def update_score(score):
    value = score_font.render("Current Score: " + str(score), True, colorSec)
    screen.blit(value, [50, 50])

class Snake():

    def __init__(self):
        self.snake_blocks = [(screen_width/2, 420), (screen_width/2 - 1*grid_size, 420), (screen_width/2 - 2*grid_size, 420)] # idx 0 is the head, the rest is the body
        self.last_tail = (0,0)
        self.score = 0
        self.direction = (1,0)
        self.alive = True

    def check_dead(self, new_head):
        return new_head[0] < 0 or new_head[1] < 0 or new_head[0] > screen_width - grid_size or new_head[1] > screen_height - grid_size or new_head in self.snake_blocks[1:]

    def move(self, direction = None):
        
        if direction == None:
            direction = self.direction
        
        # check not moving backwards or some shit
        if (direction[0] == -self.direction[0] and direction[0] != 0) or (direction[1] == -self.direction[1] and direction[1] != 0):
            pass
        else:
            # add head block
            current_head = self.snake_blocks[0]
            new_head = (current_head[0] + direction[0] * grid_size, current_head[1] + direction[1] * grid_size)
            self.snake_blocks.insert(0, new_head)
            self.last_tail = self.snake_blocks.pop()
            # change direction
            self.direction = direction

        # check dead (run into own body or go out of screen)
        if self.check_dead(self.snake_blocks[0]):
            self.alive = False


    def eat_food(self, food):
        self.score = self.score + food.score

    def get_score(self):
        return self.score


class Food():
    def __init__(self, position = (0,0)):
        self.position = position
        self.score = 1
        self.check_eaten = False

def render_food(food: Food): # Implement after we figure out pygame
    pass

def make_food():
    position = (random.randint(0,640), random.randint(0,640))
    food = Food(position)
    render_food(food)

def setup():

    snake = Snake()

    while True:
        clock.tick(5)
        direction = None
        
        update_score(snake.score)
        #increase length when eat, call your score
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (1, 0)
        snake.move(direction)
        # pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))

        screen.blit(checker, (0,100))
        for block in snake.snake_blocks:
            pygame.draw.rect(screen,colorSnake,[block[0],block[1],grid_size,grid_size])
        
        # TODO: Heiiiiiiii remember to change this shit
        if snake.alive == False:
            sys.exit()
        pygame.display.update()
    #     if eating food, increase score and leave tail alone, else remove tail
    

def main():
    setup()

if __name__ == '__main__':
    main()