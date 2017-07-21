# coding:utf-8

import pygame.font


class Button(object):

    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.width1, self.height1 = 300, 80
        self.button_color = (102, 255, 52)
        self.text_color = (255, 255, 255)
        self.rect1 = pygame.Rect(600, 200, self.width1, self.height1)
        self.rect1.center = self.screen_rect.center
        self.prep_msg("GAME OVER")

    def prep_msg(self, game_over_msg):
        self.game_over_image = self.font.render(game_over_msg, True, self.text_color,\
                                                self.button_color)
        self.game_over_image_rect = self.game_over_image.get_rect()
        self.game_over_image_rect.center = self.rect1.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect1)
        self.screen.blit(self.game_over_image, self.game_over_image_rect)
