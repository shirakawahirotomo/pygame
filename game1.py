##左キー押したらそっちの方に動くプログラム
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

background = pg.image.load("background.png").convert_alpha()  # 背景画像の取得
rect_bg = background.get_rect()

while True:




    key = pg.key.get_pressed()
    if(key[pg.K_RIGHT]):##右キー押すと反応する；K_UPorDOWNもある
        print("RIGHT")
    if(key[pg.K_LEFT]):
        print("LEFT")
    if(key[pg.K_UP]):
        print("UP")

    pg.display.update()
    pg.time.Clock().tick(60)
    screen.fill(pg.Color("WHITE"))
    screen.blit(background, rect_bg)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()