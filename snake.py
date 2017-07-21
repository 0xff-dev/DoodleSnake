#!/usr/bin/env python
# coding=utf-8

from copy import deepcopy


class Snake(object):

    def __init__(self):
        self.snakeList = [[60, 60]]
        '''开始向右， wasd，代表四个方向'''
        self.direction = 'D'

    def bodylist(self):
        '''在屏幕需要画出这条蛇，每一个坐标都要画'''
        return self.snakeList

    def move(self, stop_flag):
        '''时刻要蛇移动, 先动蛇身，头部在动'''
        if stop_flag % 2 == 0:
            body_len = len(self.snakeList) - 1
            while body_len > 0 :
                self.snakeList[body_len] = deepcopy(self.snakeList[body_len - 1])
                body_len -= 1
            '''判断方向，让蛇头就移动'''
            self.update()

    def eatfood(self, foodposition):
        self.snakeList.insert(0, foodposition)

    def update(self):
        if self.direction == 'D':
            self.snakeList[0][0] += 15
        elif self.direction == 'W':
            self.snakeList[0][1] -= 15
        elif self.direction == 'A':
            self.snakeList[0][0] -= 15
        elif self.direction == 'S':
            self.snakeList[0][1] += 15
