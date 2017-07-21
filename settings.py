# codgin:utf-8

class Settings(object):

    def __init__(self):
        self.screen_width, self.screen_height = 1300, 800
        self.snake_init_dir = 'D'
        self.bg_color = (230, 230, 230)
        self.game_name = '贪吃蛇'
        self.food_score = 50
        self.snake_speed = 15
        self.stop_flag = 0 # False
        self.init()

    def init(self):
        self.sumscore = 0
        self.sum_food = 0
        with open('./highscore') as fp:
            self.high_score = int(fp.read())

    def update_speed(self):
        self.snake_speed += 1

    def check_sum_food(self):
        if self.sum_food == 5:
            self.sum_food = 0
            self.update_speed()