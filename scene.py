import pyxel
from player import Player
from pyxel import Image

a = Image()


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("assets/jump_game.pyxres")
        
        # pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        self.p1 = Player('abc')
        self.p2 = Player('abc')
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        # 两个player的移动
        if pyxel.btn(pyxel.KEY_W):
            self.p1.move(0, -1)
        elif pyxel.btn(pyxel.KEY_S):
            self.p1.move(0, 1)
        elif pyxel.btn(pyxel.KEY_A):
            self.p1.move(-1, 0)
        elif pyxel.btn(pyxel.KEY_D):
            self.p1.move(1, 0)
        elif pyxel.btn(pyxel.KEY_UP):
            self.p2.move(0, -1)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.p2.move(0, 1)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.p2.move(-1, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.p2.move(1, 0)
    
    def draw(self):
        pyxel.cls(0)
        self.p1.update()
        self.p2.update()
        # # 颜色变化的字体, 这个里面最多16色
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        # # 将xy处将iamge0的左上角+wh 描绘上去
        # pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()
