from random import random
from math import floor
from raylib import DrawRectangle
from raylib.colors import RED
from component import Component

class Apple(Component):

    def __init__(self, cell_size: int, map_size: int):
        super().__init__(1)
        self.x = -1
        self.y = -1
        self.collected = True
        self.cell_size = cell_size
        self.map_size = map_size

    def component_update(self, delta_time: float):
        if self.collected:
            self.x = floor(random() * self.map_size)
            self.y = floor(random() * self.map_size)
            self.collected = False

    def component_draw(self):
        DrawRectangle(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size, RED)