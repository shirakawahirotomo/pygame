# 1.ゲームの準備をする
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))
## 自機データ
myimg = pg.image.load("images/myship.png")
myimg = pg.transform.scale(myimg, (50, 50))
myrect = pg.Rect(400, 500, 50, 50)
## 弾データ
bulletimg = pg.image.load("images/bullet.png")
bulletimg = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16)
## UFOデータ
ufoimg = pg.image.load("images/UFO.png")
ufoimg = pg.transform.scale(ufoimg, (50, 50))
ufos = []
for i in range(10):
    ux = random.randint(0,800)
    uy = -100 * i
    ufos.append(pg.Rect(ux, uy, 50, 50))

## ゲームステージ
def gamestage():
    # 3.画面を初期化する
    screen.fill(pg.Color("NAVY"))
    # 4.ユーザーからの入力を調べる
    (mx, my) = pg.mouse.get_pos()
    mdown = pg.mouse.get_pressed()
    # 5.絵を描いたり、判定したりする
    ## 自機の処理
    myrect.x = mx - 25
    screen.blit(myimg, myrect)
    ## 弾の処理
    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x + 25 - 8 
        bulletrect.y = myrect.y
        pg.mixer.Sound("sounds/beam.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y += -15
        screen.blit(bulletimg, bulletrect)
    ## UFOの処理
    for ufo in ufos:
        ufo.y += 10
        screen.blit(ufoimg, ufo)
        if ufo.y > 600:
            ufo.x = random.randint(0,800)
            ufo.y = -100

# 2.この下をずっとループする
while True:
    gamestage()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()