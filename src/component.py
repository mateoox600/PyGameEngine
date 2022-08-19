from __future__ import annotations
from typing import Callable
from abc import ABC

class Component(ABC):

    def __init__(self, z_index=0):
        self.z_index = z_index
        self._update = []
        self._draw: dict[int, list[Callable]] = {}
        self._components: dict[int, list[Component]] = {}

    def component_update(self, delta_time: float):
        pass

    def component_draw(self):
        pass

    def update(self, function: Callable):
        self._update.append(function)

    def draw(self, *_args, **kwargs):
        z_index = kwargs['z_index'] if 'z_index' in kwargs else 0

        def draw_inner(func):
            if z_index in self._draw:
                self._draw[z_index].append(func)
            else:
                self._draw[z_index] = [func]

        return draw_inner

    def add_component(self, *components: Component):
        for component in components:
            if component.z_index in self._components:
                self._components[component.z_index].append(component)
            else:
                self._components[component.z_index] = [component]

    def call_update(self, delta_time: float):
        self.component_update(delta_time)

        for update_call in self._update:
            update_call(delta_time)

        for _, children in sorted(self._components.items()):
            for child in children:
                child.call_update(delta_time)

    def call_draw(self):
        self.component_draw()

        for z_index, draw_calls in sorted(self._draw.items()):
            for draw_call in draw_calls:
                draw_call()

        for _, children in sorted(self._components.items()):
            for child in children:
                child.call_draw()