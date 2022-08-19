from math import floor
from raylib import DrawLine
from raylib.colors import BLACK
from engine import Engine
from snake import Snake
from apple import Apple

screen_width = 800
screen_height = 450
cell_size = 25
map_size = floor(min(screen_width, screen_height) / cell_size)

engine = Engine(screen_width, screen_height, "Testing Game Engine")

snake = Snake(floor(map_size / 2), floor(map_size / 2), cell_size, map_size)
apple = Apple(cell_size, map_size)

engine.add_component(snake, apple)

@engine.update
def main_update(delta_time: float):
    next_snake_x, next_snake_y = snake.get_next_position()
    if len(snake.cases) < 3:
        snake.extending = True
    elif snake.should_move(delta_time) and next_snake_x == apple.x and next_snake_y == apple.y:
        apple.collected = True
        snake.extending = True

@engine.draw()
def main_draw():
    for i in range(map_size + 1):
        DrawLine(i * cell_size, 0, i * cell_size, map_size * cell_size, BLACK)
    for j in range(map_size + 1):
        DrawLine(0, j * cell_size, map_size * cell_size, j * cell_size, BLACK)

engine.start()