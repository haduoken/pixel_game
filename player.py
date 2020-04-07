import pyxel


class Player:
    def __init__(self, type):
        self.position = [0, 0]
        self.animation_type = 'stand'
        self.player_animation = {}
        pass
    
    def move(self, speed_x, speed_y):
        self.position[0] += speed_x
        self.position[1] += speed_y
        pass
    
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
