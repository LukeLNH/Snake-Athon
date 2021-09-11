import pygame


class Snake():

    snake_blocks = [] # idx 0 is the head, the rest is the body

    def __init__(self):
        # set initial length of snake
        pass

    def move(self):
        pass

    def eat_food(self):
        # has to grow after eating
        pass

    def check_dead(self):
        pass

    def get_score(self):
        return len(self.snake_blocks)


class Food():
    position = (0,0)
    score = 100
    check_eaten = False

    def __init__(self):
        pass


def make_food():
    pass

def display_score():
    pass

def setup():
    # Gonna need a shit ton of helper functions :)
    pass

def start_game():
    # where the main while loop will be
    pass

def main():
    setup()
    start_game()

if __name__ == '__main__':
    main()