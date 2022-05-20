##シューティングゲーム
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))

myimg = pg.image.load("images/myship.png")##画像読み込み
myimg = pg.transform.scale(myimg, (50, 50)) ##50,50がぞにする
myrect = pg.Rect(400, 500, 50, 50) ##50, 50は上に合わせてる

bulletimg = pg.image.load("images/bullet.png")
Bulletimg = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16) ##画面外に16×16画素で設定

def gamestage():
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos() ##マウスの位置に従ってmx, myにその座標が入力される
    mdown = pg.mouse.get_pressed()

    myrect.x = mx - 25
    screen.blit(myimg, myrect)

    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x - 50 ##球のx軸の位置
        bulletrect.y = myrect.y
        pg.mixer.Sound("sounds/pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y += -50 ##球の速さ
        screen.blit(bulletimg, bulletrect)

while True:
	gamestage()

	pg.display.update()
	pg.time.Clock().tick(60)
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()