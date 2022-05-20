##シューティングゲーム
##画面が居にUFOを設定してy軸に沿って下の方にずらしていく処理
##UFOを10個用意する
##x軸をランダムにする
##1機目、2機目、3機目をy軸を-100, -200, -300....にずらしていく
import pygame as pg, sys
import random
pg.init()
screen = pg.display.set_mode((800, 600))

myimg = pg.image.load("images/myship.png")##画像読み込み
myimg = pg.transform.scale(myimg, (50, 50)) ##50,50がぞにする
myrect = pg.Rect(400, 500, 50, 50) ##50, 50は上に合わせてる

bulletimg = pg.image.load("images/bullet.png")
bulletimg = pg.transform.scale(bulletimg, (16, 16))
bulletrect = pg.Rect(400, -100, 16, 16) ##画面外に16×16画素で設定

ufoimg = pg.image.load("images/UFO.png")##UFOの画像を読み込み
ufoimg = pg.transform.scale(ufoimg, (50, 50))##50×50画素の画像にスケーリングする
ufos = []##空のリストを作っている
for i in range(50):
    ux = random.randint(0, 800)##x軸は0から800までの数字をランダムで出力
    uy = -100*i##1~10を掛けていく
    ufos.append(pg.Rect(ux, uy, 50, 50))##ufosに付け加えていく。pg.Rectで貼り付けていってそれを加えている。


def gamestage():
    screen.fill(pg.Color("NAVY"))
    (mx, my) = pg.mouse.get_pos() ##マウスの位置に従ってmx, myにその座標が入力される
    mdown = pg.mouse.get_pressed()

    myrect.x = mx - 25
    screen.blit(myimg, myrect)

    if mdown[0] and bulletrect.y < 0:
        bulletrect.x = myrect.x +25 -8  ##球のx軸の位置
        bulletrect.y = myrect.y
        pg.mixer.Sound("sounds/pi.wav").play()
    if bulletrect.y >= 0:
        bulletrect.y += -50 ##球の速さ
        screen.blit(bulletimg, bulletrect)
    ##uyをfor文で回せばufoが降りてくる
    '''for ufo in ufos:
        ufo.y += 2
        screen.blit(ufoimg, ufo)##出力する
        if ufo.y > 600:
            ufo.x = random.randint(0, 800)
            ufo.y = -100'''

    for i in range(30):##自分で書いたコード
        ufos[i].y += 10
        if ufos[i].y >= 600:
            ufos[i].y -= 700
            ufos[i].x = random.randint(0, 800)
        screen.blit(ufoimg, ufos[i]) #描写する

            

while True:
	gamestage()

	pg.display.update()
	pg.time.Clock().tick(60)
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()