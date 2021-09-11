import pygame
import random

screen_width = 640
screen_height = 640
grid_size = 30

class Snake():

    def __init__(self):
        self.snake_blocks = [(screen_width/2, screen_height/2), (screen_width/2 - 1*grid_size, screen_height/2), (screen_width/2 - 2*grid_size, screen_height/2)] # idx 0 is the head, the rest is the body
        self.last_tail = (0,0)
        self.score = 0
        self.direction = (1,0)
        self.alive = True

    def check_dead(self, new_head):
        return new_head[0] < 0 or new_head[1] < 0 or new_head[0] > screen_width - grid_size or new_head[1] > screen_height - grid_size or new_head in self.snake_blocks[1:]

    def move(self):
        for event in pygame.event.get():
            direction = self.direction
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP:
                    direction = (0, -1)
                elif event.type == pygame.K_DOWN:
                    direction = (0, 1)
                elif event.type == pygame.K_LEFT:
                    direction = (-1, 0)
                elif event.type == pygame.K_RIGHT:
                    direction = (1, 0)
        
        # check not moving backwards or some shit
        if direction[0] == -self.direction[0] or direction[1] == -self.direction[1]:
            pass
        else:
            # add head block
            current_head = self.snake_blocks[0]
            new_head = (current_head[0] + direction[0] * grid_size, current_head[1] + direction[1] * grid_size)
            self.snake_blocks.insert(0, new_head)
            self.last_tail = self.snake_blocks.pop(-1)
            # change direction
            self.direction = direction

        # check dead (run into own body or go out of screen)
        if self.check_dead(new_head):
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

def display_score():
    pass

def setup():
    # Gonna need a shit ton of helper functions :)
    # pygame.init()
    # clock = pygame.time.Clock()
    # screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    # surface = pygame.Surface(screen.get_size())
    # surface = surface.convert()

    # for x in range(screen_height):
    #     for y in range(screen_width):
    #         rect = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
    #         pygame.draw.rect(surface, (0,0,255), rect)
    
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             break
    #     clock.tick(10)
    #     snake.move()
    #     if eating food, increase score and leave tail alone, else remove tail
    pass

def main():
    setup()

if __name__ == '__main__':
    main()