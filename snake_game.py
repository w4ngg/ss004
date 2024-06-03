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
start_bg = transform.scale(image.load('start_bg.png'), (window_x, window_y))
end_bg = transform.scale(image.load('end.jpg'), (window_x, window_y))
start_sound = pygame.mixer.Sound('start_sound.mp3')
end_sound = pygame.mixer.Sound('end_sound.wav.mp3')
eat_sound = pygame.mixer.Sound('eat.wav.mp3')
# khai bao game window
pygame.display.set_caption('Snacks Game')
game_window = pygame.display.set_mode((window_x, window_y))

def game_over():
    # Gọi hàm end_game
    end_game()
def end_game():
    end_sound.play()
    while True:
        game_window.blit(end_bg,(0,0))
        font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = font.render('Your Score is : ' + str(score), True, black)
        instruction_surface = font.render('Press ESC to quit', True, black)
        game_over_rect = game_over_surface.get_rect()
        instruction_rect = instruction_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        instruction_rect.midtop = (window_x / 2, window_y / 2)
        game_window.blit(game_over_surface, game_over_rect)
        game_window.blit(instruction_surface, instruction_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_sound.stop()
                    pygame.quit()
                    quit()

def start_game():
    start_sound.play()
    while True:
        game_window.blit(start_bg,(0,0))
        font = pygame.font.SysFont('times new roman', 50)
        welcome_surface = font.render('Welcome to Snake Game', True, white)
        instruction_surface = font.render('Press SPACE to start', True, white)
        welcome_rect = welcome_surface.get_rect()
        instruction_rect = instruction_surface.get_rect()
        welcome_rect.midtop = (window_x / 2, window_y / 4)
        instruction_rect.midtop = (window_x / 2, window_y / 2)
        game_window.blit(welcome_surface, welcome_rect)
        game_window.blit(instruction_surface, instruction_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_sound.stop()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
start_game()