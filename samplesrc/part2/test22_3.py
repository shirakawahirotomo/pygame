# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
imageR = pg.image.load("images/playerR.png")
imageL = pg.transform.flip(imageR, True, False)
myrect = pg.Rect(300, 200, 80, 100)
rightFlag = True

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    vx = 0
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 5.絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx = 5
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -5
        rightFlag = False
    myrect.x = myrect.x + vx
    if rightFlag:
        screen.blit(imageR, myrect)
    else:
        screen.blit(imageL, myrect)
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            