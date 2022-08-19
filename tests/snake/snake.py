from enum import Enum
from raylib import DrawRectangle, IsKeyPressed, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from raylib.colors import GREEN, BLUE
from component import Component

class Direction(Enum):
    DOWN = 0
    LEFT = 1
    UP = 2
    RIGHT = 3

class Snake(Component):

    def __init__(self, start_x: int, start_y: int, cell_size: int, map_size: int):
        super().__init__(1)
        self.x = start_x
        self.y = start_y
        self.cell_size = cell_size
        self.map_size = map_size
        self.direction = Direction.DOWN
        self.last_move_direction = None
        self.cases = []
        self.extending = False
        self.move_timer = 0
        self.died = False

    def get_next_position(self):
        next_x = self.x
        next_y = self.y
        if self.direction == Direction.DOWN:
            next_y += 1
        elif self.direction == Direction.UP:
            next_y -= 1
        elif self.direction == Direction.RIGHT:
            next_x += 1
        elif self.direction == Direction.LEFT:
            next_x -= 1
        return next_x, next_y

    def should_move(self, delta_time_offset=0):
        return self.move_timer + delta_time_offset >= 0.75

    def component_update(self, delta_time: float):
        if self.died:
            return

        if IsKeyPressed(KEY_DOWN) and self.last_move_direction != Direction.UP:
            self.direction = Direction.DOWN
        elif IsKeyPressed(KEY_UP) and self.last_move_direction != Direction.DOWN:
            self.direction = Direction.UP
        elif IsKeyPressed(KEY_RIGHT) and self.last_move_direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        elif IsKeyPressed(KEY_LEFT) and self.last_move_direction != Direction.RIGHT:
            self.direction = Direction.LEFT

        self.move_timer += delta_time
        if self.should_move():
            self.move_timer = 0
            next_x, next_y = self.get_next_position()
            self.x = next_x
            self.y = next_y

            if self.x < 0 or self.x >= self.map_size or self.y < 0 or self.y >= self.map_size:
                self.died = True
                return

            self.last_move_direction = self.direction
            self.cases.append((self.x, self.y))
            if not self.extending:
                self.cases.pop(0)
            else:
                self.extending = False

    def component_draw(self):
        for x, y in self.cases:
            DrawRectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, BLUE if self.died else GREEN)