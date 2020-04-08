import pyxel
from math import sqrt


class Player:
    def __init__(self, name):
        self.position = [0, 0]
        self.animation_type = 'stand'
        self.player_animation = {}
        self.name = name
        self.last_direction = ''
        # 1pix/s
        self.speed = 30
        pass
    
    def move(self, direction):
        dt = 1.0 / pyxel.DEFAULT_FPS
        speed_x, speed_y = 0, 0
        should_format_number = False
        if direction != self.last_direction:
            should_format_number = True
            self.last_direction = direction
        
        if direction == 'up':
            speed_y = -self.speed
        elif direction == 'down':
            speed_y = self.speed
        elif direction == 'left':
            speed_x = -self.speed
        elif direction == 'right':
            speed_x = self.speed
        
        elif direction == 'left-up':
            speed_x = -self.speed * 0.707
            speed_y = -self.speed * 0.707
        elif direction == 'right-up':
            speed_x = self.speed * 0.707
            speed_y = -self.speed * 0.707
        elif direction == 'left-down':
            speed_x = -self.speed * 0.707
            speed_y = self.speed * 0.707
        elif direction == 'right-down':
            speed_x = self.speed * 0.707
            speed_y = self.speed * 0.707
        
        self.position[0] += (speed_x * dt)
        self.position[1] += (speed_y * dt)
        if should_format_number:
            self.position[0] = int(self.position[0])
            self.position[1] = int(self.position[1])
        print(self.name, 'speed: ', speed_x, speed_y, ' position: ', self.position)
    
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
