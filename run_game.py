#!/usr/bin/env python
# coding=utf-8

import pygame
from snake import Snake
from food import Food
from pygame.time import Clock
import game_function as gf
from settings import Settings
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption(setting.game_name)
    snake = Snake()
    food = Food()
    sb = ScoreBoard(screen, setting)
    snake.direction = setting.snake_init_dir
    clock = Clock()
    while True:
        screen.fill(setting.bg_color)
        gf.check_events(snake, setting)
        gf.draw_snake_food(screen, snake.bodylist(), food.food_pos())
        # 不设置一下，这条蛇要飞
        clock.tick(setting.snake_speed)
        snake.move(setting.stop_flag)
        gf.is_game_over(screen, snake.snakeList[0], snake.bodylist(), setting)
        gf.check_eat_food(snake, sb, food, setting)
        gf.update_screen(sb)


def restart():
    run_game()


if __name__ == '__main__':
    run_game()
