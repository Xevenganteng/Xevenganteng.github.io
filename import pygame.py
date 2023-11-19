import pygame
import sys
import os
import random

pygame.init()

# Screen settings
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Snake settings
snake_size = 20
snake_speed = 15

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

class Snake:
    # ... (implement the Snake class here)

class Food:
    # ... (implement the Food class here)

def game_loop():
    snake = Snake()
    food = Food()
    score = 0

    while True:
        # Event handling