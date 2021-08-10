import pygame as pg
from enum import IntEnum
from random import randrange
from colors import Color


class Direct(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class DirectionError(Exception):
    ...


class Snake():
    def __init__(self, arena, start_size = 3):
        self._direct = Direct(randrange(0, 4))
        self._arena = arena
        init = {
            Direct.UP: [(self._arena[0] // 2, self._arena[1] // 2 + i) for i in range(start_size)],
            Direct.RIGHT: [(self._arena[0] // 2 - i, self._arena[1] // 2) for i in range(start_size)],
            Direct.DOWN: [(self._arena[0] // 2, self._arena[1] // 2 - i) for i in range(start_size)],
            Direct.LEFT: [(self._arena[0] // 2 + i, self._arena[1] // 2) for i in range(start_size)],
        }
        self._body = init[self._direct]

    def __len__(self):
        return len(self._body)

    def __iter__(self):
        self._cursor = 0
        return self

    def __nex__(self):
        try:
            element = self._body[self._cursor]
        except IndexError:
            del self._cursor 
            raise StopIteration
        self.cursor += 1
        return element

    @property
    def direction(self):
        return self._direct

    @direction.setter
    def direction(self, value):
        if isinstance(value, Direct):
            self._direct = value
        else:
            raise ValueError("'value' is not 'Direction'.")

    @staticmethod
    def raise_(ex):
        raise ex

    def step(self, food):
        steps = {
            Direct.UP: (lambda x, y: (x, y-1) if y>0 else self.raise_(DirectionError())),
            Direct.RIGHT: (lambda x, y: (x+1, y) if x<self._arena[0] - 1 else self.raise_(DirectionError())),
            Direct.DOWN: (lambda x, y: (x, y+1) if x<self._arena[1] - 1 else self.raise_(DirectionError())),
            Direct.LEFT: (lambda x, y: (x-1, y) if y>0 else self.raise_(DirectionError())), 
        }
        try:
            x, y = steps[self._direct](*self._body[0])
        except DirectionError:
            return False
        if(x, y) in self._body:
            return False
        if(x, y) != food:
            del self._body[-1]
        self._body.insert(0, (x, y))
        return True

    def check(self, block):
        return block in self._body


class Arena(pg.Surface):
    def __init__(self, win_size, box_size, area):
        super().__init__(win_size)
        self._win_size = win_size
        self._box = box_size
        self._area = area
        self._bg_color = Color.ORANGE
        self._food_color = Color.RED
        self._snake_color = Color.WHITE
        self._head_color = Color.BLUE
        self._end_game = False
        #self._food = None
        self.snake = Snake(self._area)
        self.fill(self._bg_color)
        self.add_food()
        self.draw_snake()
        self.draw_food()

    @property
    def is_end(self):
        return self._end_game

    def draw_snake(self):
        for block, color in zip(self.snake, [self._head_color] + [self._snake_color] * (len(self.snake) - 1)):
            x, y = block
            x_s = x * self._box + 1
            y_s = y * self._box + 1
            x_e = x_s + self._box -1
            y_e = y_s + self._box -1
            pg.draw.rect(self, color, [x_s, y_s, x_e, y_e])

    def draw_food(self):
        x, y = self._food
        x_s = x * self._box + 1
        y_s = y * self._box + 1
        x_e = x_s + self._box - 1
        y_e = y_s + self._box - 1
        pg.draw.rect(self, self._food_color, [x_s, y_s, x_e, y_e])

    def add_food(self):
        self._food = (
            randrange(0, self._win_size[0]),
            randrange(0, self._win_size[1])
        )
        while self.snake.check(self._food):
            self._food = (
            randrange(0, self._win_size[0]),
            randrange(0, self._win_size[1])
        )

    def update(self, direct):
        if direct is not None:
            self.snake.direction = direct
        self.snake.direction = direct
        if self.snake.step(self._food):
            if self.snake.step(self._food):
                self.add._food()
            self.draw_food()
            self.draw_snake()
        else:
            #end game
            self._end_game = True

