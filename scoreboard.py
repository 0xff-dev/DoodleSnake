# coding:utf-8

import pygame.font


class ScoreBoard(object):

    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        round_score = int(round(self.setting.sumscore, -1))
        score_str = "score:{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color,\
                                              self.setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 1000
        self.score_rect.top = 20

    def prep_high_score(self):
        round_high_score = int(round(self.setting.high_score, -1))
        high_scroe_str = "highSc:{:,}".format(round_high_score)
        self.high_score_image = self.font.render(high_scroe_str, True, \
                                                 self.text_color, self.setting.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 1000
        self.high_score_rect.top = 50

    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
