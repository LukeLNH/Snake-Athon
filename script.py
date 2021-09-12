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
colorFood = (240, 55, 165)

size = width, height = 640, 740
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

class Snake():
    def __init__(self):
        self.snake_blocks = [(screen_width/2, 420), (screen_width/2 - 1*grid_size, 420), (screen_width/2 - 2*grid_size, 420), (screen_width/2 - 3*grid_size, 420), (screen_width/2 - 4*grid_size, 420)] # idx 0 is the head, the rest is the body
        self.last_tail = (0,0)
        self.score = 0
        self.direction = (1,0)
        self.alive = True

    def get_head_pos(self):
        return self.snake_blocks[0]

    def check_dead(self, new_head):
        return new_head[0] < MINx or new_head[1] < MINy or new_head[0] > MAXx - grid_size or new_head[1] > MAXy - grid_size or new_head in self.snake_blocks[1:]

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
        # grow the snek
        self.snake_blocks.append(self.last_tail)

    def get_score(self):
        return self.score


class Food():
    def __init__(self, position = (0,0)):
        self.position = position
        self.score = 1
        self.check_eaten = False

def render_food(food: Food): # Implement after we figure out pygame
    pygame.draw.rect(screen,colorFood,[MINx + food.position[0], MINy + food.position[1], grid_size,grid_size])

# Spawnning in snake bug is still here
def make_food(snake):
    while True:
        position = (random.randint(0,19) * grid_size, random.randint(0,19) * grid_size)
        scaled_pos = (position[0] + MINx, position[1] + MINy)
        if scaled_pos not in snake.snake_blocks:
            break
    food = Food(position)
    return food

def setup():
    active_game = False
    snake = Snake()
    food = make_food(snake)
    
    screen.fill(colorPrim)
    pygame.draw.rect(screen, colorSec, pygame.Rect(200, 300, 240, 50))
    value = score_font.render("PLAY", True, colorPrim)
    screen.blit(value, [245, 306])
    pygame.display.update()
    welcome = True
    while welcome:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Click")
                mouse = pygame.mouse.get_pos()
                if (200 <= mouse[0] <= 440) and (300 <= mouse[1] <= 350):
                    welcome = False
                    # screen.blit(checker, (0,100))
                    # value = score_font.render("Current Score: %s      " % str(snake.score), True, colorSec, colorPrim)
                    # screen.blit(value, [50, 50])
                    pygame.display.update()

    while True:
        if active_game:
            clock.tick(5)
            direction = None
            value = score_font.render("Current Score: %s      " % str(snake.score), True, colorSec, colorPrim)
            screen.blit(value, [50, 50])
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

            snake_head_pos = snake.get_head_pos()
            snake_head_pos = (snake_head_pos[0] - MINx, snake_head_pos[1] - MINy)
            if food.position == snake_head_pos:
                snake.eat_food(food)
                food = make_food(snake)
            
            render_food(food)
            for block in snake.snake_blocks:
                pygame.draw.rect(screen,colorSnake,[block[0],block[1],grid_size,grid_size])
            
            if snake.alive == False:
                score = snake.score
                active_game = False
                del snake
                del food
                pygame.draw.rect(screen, colorPrim, pygame.Rect(0, 0, 640, 740))
                pygame.draw.rect(screen, colorSec, pygame.Rect(200, 300, 240, 50))
                
                value = score_font.render("Current Score: " + str(score), True, colorSec)
                screen.blit(value, [200, 250])

                value = score_font.render("RESTART", True, colorPrim)
                screen.blit(value, [245, 306])
            pygame.display.update()
        
        else: # display the score + restart button
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if (200 <= mouse[0] <= 440) and (300 <= mouse[1] <= 350):
                        active_game = True
                        snake = Snake()
                        food = make_food(snake)


    

def main():
    setup()

if __name__ == '__main__':
    main()