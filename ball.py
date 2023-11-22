from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1737)
        self.y = y if y else random.randint(100, 1090)

    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(sx, sy)

    def set_background(self, bg):
        self.bg = bg

    def update(self):
        self.x = clamp(50.0, self.x, self.bg.w - 50.0)
        self.y = clamp(50.0, self.y, self.bg.h - 50.0)
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                game_world.remove_object(self)
                pass
            case 'zombie:ball':
                other.ball = self