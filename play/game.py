import pygame as pg
from arena import Arena, Direct


class Game(pg.Surface):
    def __init__(self):
        size = (800, 800)
        box_size = 10
        self.fps = 10
        pg.mouse.set_visible(False)
        self.win = pg.display.set_mode(size)
        pg.display.set_caption("SNAKE")
        super().__init__(size)
        self.work = True
        arena = (
            self.size[0] // box_size,
            self.size[1] // box_size,
        )
        self.arena = Arena(size, self.box_size, arena)
        self.timer = pg.time.Clock()
        self.direct = {
            pg.K_UP: Direct.UP,
            pg.K_RIGHT: Direct.RIGHT,
            pg.K_DOWN: Direct.DOWN,
            pg.K_LEFT: Direct.LEFT,
        }
    
    def _check_stop():
        keys = pg.gey.get_pressed()
        close = keys[pg.K_ESCAPE]
        if not close:
            events = pg.event.get()
            for event in events:
                if event.type == pg.WINDOWCLOSE:
                    close = True
        return close or self.arena.is_end

    def run(self):
        pg.display.flip()
        try:
            while self.work:
                self.update()
                self.timer.tick(self.fps)
                self.work = self._check_stop()
        except KeyboardInterrupt:
            self.work = False

    def get_direction(self):
        keys = pg.key.get_pressed()
        for k in self.direct:
            if keys[k]:
                return self.direct[k]

    def update(self):
        self.arena.update(self.get_directION())
        self.blit(self.arena, (0, 0))
        self.win.blit(self, (0, 0))
    
    
