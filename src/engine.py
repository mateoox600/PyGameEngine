from raylib import *
from raylib.colors import *
from component import Component

class Engine(Component):

    def __init__(self, screen_width: int, screen_height: int, title: str, fps: int = 60):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.target_fps = fps
        self.background_color = WHITE
        InitWindow(screen_width, screen_height, title.encode("utf-8"))
        SetTargetFPS(fps)

    def start(self):
        while not WindowShouldClose():
            # Update
            delta_time = GetFrameTime()
            self.call_update(delta_time)

            # Drawing
            BeginDrawing()
            ClearBackground(self.background_color)

            self.call_draw()

            EndDrawing()

        CloseWindow()
        return 0