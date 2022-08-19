from engine import Engine
from component import Component
from raylib import DrawRectangle
from raylib.colors import BLACK, RED
from math import floor

engine = Engine(800, 450, "Testing Game Engine")

class Square(Component):

    def __init__(self, x, y, width, height, color, z_index=0):
        super().__init__(z_index)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def component_draw(self):
        DrawRectangle(floor(self.x), floor(self.y), self.width, self.height, self.color)

black_square = Square(10, 50, 10, 10, BLACK)
red_square = Square(15, 50, 10, 10, RED, 1)

engine.add_component(black_square, red_square)

x_frame_offset = 0

@engine.update
def main_update(delta_time: float):
    global x_frame_offset
    x_frame_offset = 100 * delta_time

@engine.draw()
def main_draw():
    black_square.x += x_frame_offset
    red_square.x += x_frame_offset

engine.start()