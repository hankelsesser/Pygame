import pygame as pg, sys
pg.init()

size = width, height =  750, 700
speed = [2, 2]
black = 0, 0, 0

screen = pg.display.set_mode(size)



while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    pg.draw.ellipse(screen, (255, 10, 10), pg.Rect(30, 30, 60, 60))

    # screen.fill(black)
    pg.display.flip()