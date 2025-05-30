import pygame
import time
import random
import math

pygame.init()

# Constants
window_x = 720
window_y = 480
margin = 40
snake_size = 20
snake_speed = 10.0  # Fixed speed

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Setup
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('PROŽDRLJIVA ZMIJA')
fps = pygame.time.Clock()

# Load images
background = pygame.transform.scale(pygame.image.load('zmija.png'), (window_x, window_y))
pause_image = pygame.transform.scale(pygame.image.load('pauza.png'), (30, 30))

head_img = pygame.transform.scale(pygame.image.load('head.jpg.png'), (snake_size, snake_size))
body_img = pygame.transform.scale(pygame.image.load('body.jpg.png'), (snake_size, snake_size))
tail_img = pygame.transform.scale(pygame.image.load('tail.jpg.png'), (snake_size, snake_size))

food_images = [
    pygame.transform.scale(pygame.image.load('hamburger.png'), (snake_size+5, snake_size+5)),
    pygame.transform.scale(pygame.image.load('kola.png'), (snake_size+5, snake_size+5)),
    pygame.transform.scale(pygame.image.load('pomfrit.png'), (snake_size+5, snake_size+5)),
    pygame.transform.scale(pygame.image.load('happymeal.png'), (snake_size+5, snake_size+5)),
    pygame.transform.scale(pygame.image.load('chickenbox.png'), (snake_size+5, snake_size+5)),
    pygame.transform.scale(pygame.image.load('sladoled.png'), (snake_size+5, snake_size+5))
]

def random_food_position():
    x = random.randrange(margin, window_x - margin, snake_size)
    y = random.randrange(margin, window_y - margin, snake_size)
    return [x, y]

def show_score(color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Bodovi : ' + str(score), True, color)
    game_window.blit(score_surface, (margin, margin // 4))

def start_screen():
    waiting = True
    start_button_rect = pygame.Rect(window_x // 2 - 75, window_y // 2, 150, 50)
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    waiting = False

        game_window.blit(background, (0, 0))
        title_font = pygame.font.SysFont('times new roman', 50)
        title_surface = title_font.render('PROŽDRLJIVA ZMIJA', True, black)
        title_rect = title_surface.get_rect(center=(window_x // 2, window_y // 3))
        game_window.blit(title_surface, title_rect)

        pygame.draw.rect(game_window, green, start_button_rect)
        button_font = pygame.font.SysFont('times new roman', 30)
        button_surface = button_font.render('POČETAK', True, black)
        button_rect = button_surface.get_rect(center=start_button_rect.center)
        game_window.blit(button_surface, button_rect)

        pygame.display.update()
        fps.tick(15)

def pause_screen():
    resume_button_rect = pygame.Rect(window_x // 2 - 75, window_y // 2, 150, 50)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button_rect.collidepoint(event.pos):
                    paused = False

        pause_overlay = pygame.Surface((window_x, window_y))
        pause_overlay.set_alpha(150)
        pause_overlay.fill(black)
        game_window.blit(pause_overlay, (0, 0))

        pause_font = pygame.font.SysFont('times new roman', 50)
        pause_text = pause_font.render('PAUZA', True, white)
        pause_rect = pause_text.get_rect(center=(window_x // 2, window_y // 3))
        game_window.blit(pause_text, pause_rect)

        pygame.draw.rect(game_window, green, resume_button_rect)
        button_font = pygame.font.SysFont('times new roman', 30)
        resume_text = button_font.render('NASTAVI', True, black)
        resume_rect = resume_text.get_rect(center=resume_button_rect.center)
        game_window.blit(resume_text, resume_rect)

        pygame.display.update()
        fps.tick(15)

def game_over_screen(score):
    waiting = True
    kraj_button_rect = pygame.Rect(window_x // 2 - 150, window_y // 2, 120, 50)
    ponovi_button_rect = pygame.Rect(window_x // 2 + 30, window_y // 2, 120, 50)
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if kraj_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                if ponovi_button_rect.collidepoint(event.pos):
                    waiting = False

        game_window.blit(background, (0, 0))
        game_over_font = pygame.font.SysFont('times new roman', 40)
        over_text = game_over_font.render('Postignuti broj bodova : ' + str(score), True, black)
        over_rect = over_text.get_rect(center=(window_x // 2, window_y // 3))
        game_window.blit(over_text, over_rect)

        pygame.draw.rect(game_window, green, kraj_button_rect)
        pygame.draw.rect(game_window, green, ponovi_button_rect)
        button_font = pygame.font.SysFont('times new roman', 30)
        kraj_text = button_font.render('KRAJ', True, black)
        ponovi_text = button_font.render('PONOVI', True, black)
        kraj_text_rect = kraj_text.get_rect(center=kraj_button_rect.center)
        ponovi_text_rect = ponovi_text.get_rect(center=ponovi_button_rect.center)
        game_window.blit(kraj_text, kraj_text_rect)
        game_window.blit(ponovi_text, ponovi_text_rect)

        pygame.display.update()
        fps.tick(15)

def main_game():
    snake_position = [100, 40]
    snake_body = [[100, 40], [80, 40], [60, 40], [40, 40]]
    direction = 'RIGHT'
    change_to = direction
    score = 0

    food_position = random_food_position()
    current_food_image = random.choice(food_images)
    food_spawn = True

    pause_button_rect = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button_rect and pause_button_rect.collidepoint(event.pos):
                    pause_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= snake_size
        elif direction == 'DOWN':
            snake_position[1] += snake_size
        elif direction == 'LEFT':
            snake_position[0] -= snake_size
        elif direction == 'RIGHT':
            snake_position[0] += snake_size

        snake_body.insert(0, list(snake_position))

        if snake_position == food_position:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = random_food_position()
            current_food_image = random.choice(food_images)
            food_spawn = True

        game_window.blit(background, (0, 0))

        game_window.blit(head_img, pygame.Rect(snake_body[0][0], snake_body[0][1], snake_size, snake_size))
        for block in snake_body[1:]:
            game_window.blit(body_img, pygame.Rect(block[0], block[1], snake_size, snake_size))

        game_window.blit(current_food_image, pygame.Rect(food_position[0], food_position[1], snake_size, snake_size))

        pause_button_rect = pygame.Rect(window_x - margin - 30, margin // 4 - 5, 30, 30)
        game_window.blit(pause_image, pause_button_rect)
        show_score(black, 'times new roman', 20, score)

        if (snake_position[0] < margin or snake_position[0] >= window_x - margin or
            snake_position[1] < margin or snake_position[1] >= window_y - margin):
            running = False
        for block in snake_body[1:]:
            if snake_position == block:
                running = False

        pygame.display.update()
        fps.tick(snake_speed)

    return score

def main():
    start_screen()
    while True:
        score = main_game()
        game_over_screen(score)

if __name__ == '__main__':
    main()
