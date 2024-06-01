from pygame import *
import pygame
import time
import random
 



# chieu dai va chieu rong cua background
window_x = 900
window_y = 800
 
# RGB colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# khai bao pygame
pygame.init()

# khai bao game window
pygame.display.set_caption('Snacks Game')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS cho tro choi (frame per second)
fps = pygame.time.Clock()
 
 
# vi tri ban dau cua con ran khi bat dau tro choi
snake_position = [100, 50]
 
# than con ran
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# toc do di chuyen cua con ran
snake_speed = 15
# huong ban dau cua con ran khi tro choi bat dau
direction = 'RIGHT'
change_to = direction

##NOTE for Đạt, làm windows khi vào game và kết thúc trò chơi, âm thanh