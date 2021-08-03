import pygame as pg
from play.colors import Color

pg.init()
timer = pg.time.Clock()
fps = 60

game_scrin = pg.display.set_mode(
    (800, 600),
    pg.HWSURFACE | pg.DOUBLEBUF | pg.OPENGL,
)
pg.display.set_caption("snake")
game_scrin.fill(Color.BLUE)
work = True
while work:
    keys = pg.key.get_pressed()
    work = not keys[pg.K_ESCAPE]
    timer.tick(fps)
    events = pg.event.get()
    for ev in events:
        print(ev)
        if ev.type == pg.WINDOWCLOSE:
            work = False

pg.quit()
# __pycache__/