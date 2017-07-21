# coding:utf-8

import pygame
import sys
from button import Button
from run_game import restart


def check_events(snake, setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.ecit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, snake, setting)


def check_key_down(event, snake, setting):
    if event.key == pygame.K_RIGHT:
        snake.direction = 'D'
    elif event.key == pygame.K_LEFT:
        snake.direction = 'A'
    elif event.key == pygame.K_UP:
        snake.direction = 'W'
    elif event.key == pygame.K_DOWN:
        snake.direction = 'S'
    elif event.key == pygame.K_SPACE:
        setting.stop_flag = (setting.stop_flag + 1) % 2


def draw_snake_food(screen, snake_list, food_ps):
    for rect in snake_list:
        tmp_rect = pygame.Rect(rect[0], rect[1], 15, 15)
        pygame.draw.rect(screen, (102, 255, 52), tmp_rect)
    food_rect = pygame.Rect(food_ps[0], food_ps[1], 15, 15)
    pygame.draw.rect(screen, (102, 255, 52), food_rect)


def is_game_over(screen, snake_head, snake_list, setting):
    if snake_head[0] > 900 or snake_head[0] < 0 or snake_head[1] > 800 or \
                    snake_head[1] < 0 or snake_head in snake_list[1:]:
        screen.fill((230, 230, 230))
        button = Button(screen, setting.sumscore)
        button.draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button.rect1.collidepoint(mouse_x, mouse_y):
                    with open('./highscore', 'w') as fp:
                        fp.write(str(setting.high_score))
                    restart()
            elif event.type == pygame.QUIT:
                with open('./highscore', 'w') as fp:
                    fp.write(str(setting.high_score))
                sys.exit()


def check_eat_food(snake, sb, food, setting):
    if snake.snakeList[0] == food.food_pos():
        snake.eatfood(food.food_pos())
        setting.sum_food += 1
        sb.prep_score()
        setting.sumscore += setting.food_score
        if setting.sumscore > setting.high_score:
            setting.high_score = setting.sumscore
            sb.prep_high_score()
        setting.check_sum_food()
        food.update_food_pos(snake.bodylist())


def update_screen(sb):
    sb.draw()
    pygame.display.update()