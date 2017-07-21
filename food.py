#!/usr/bin/env python
# coding=utf-8

from random import randint


class Food(object):

    def __init__(self):
        """0,"""
        self.xy()
        self.food_position = [self.food_px, self.food_py]

    def xy(self):
        """了；留出左边的部分记录分数,在分数达到一定等级，速度加快 """
        self.food_px = randint(1, 60) * 15
        self.food_py = randint(1, 52) * 15

    def food_pos(self):
        return self.food_position

    def update_food_pos(self, snakeList):
        """食物的位置不能位于蛇身上"""
        self.xy()
        while [self.food_px, self.food_py] in snakeList:
            self.xy()
        self.food_position = [self.food_px, self.food_py]

