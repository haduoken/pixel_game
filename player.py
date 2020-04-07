import pyxel
from math import sqrt


class Player:
    def __init__(self, type):
        self.position = [0, 0]
        self.animation_type = 'stand'
        self.player_animation = {}
        self.speed = 1
        pass

    def move(self, direction):
        speed_x, speed_y = 0, 0
        if direction == 'up':
            speed_y = -self.speed
        elif direction == 'down':
            speed_y = self.speed
        elif direction == 'left':
            speed_x = -self.speed
        elif direction == 'right':
            speed_x = self.speed

        elif direction == 'up-left':

            speed_x = -self.speed * sqrt(2) / 2.0
            speed_y = -self.speed * sqrt(2) / 2.0

        elif direction == 'up-right':
            speed_x = self.speed * sqrt(2) / 2.0
            speed_y = -self.speed * sqrt(2) / 2.0
        elif direction == 'down-left':
            speed_x = -self.speed * sqrt(2) / 2.0
            speed_y = self.speed * sqrt(2) / 2.0
        elif direction == 'down-right':
            speed_x = self.speed * sqrt(2) / 2.0
            speed_y = self.speed * sqrt(2) / 2.0

        self.position[0] += speed_x
        self.position[1] += speed_y

    def act(self, type):

        self.type = type

    def update(self):

        # image = self.player_animation[self.animation_type].get_next_frame()
        pyxel.blt(
            self.position[0],
            self.position[1],
            0,
            16,
            0,
            16,
            16,
            12,
        )
