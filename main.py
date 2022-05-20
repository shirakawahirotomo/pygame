#ブロック崩しのゲーム
#左側の壁に当たった時は変化量をマイナスにする

import pygame as pg, sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))

barrect = pg.Rect(400, 500, 100, 20)

ballimg = pg.image.load("images/kaeru.png")
ballimg = pg.transform.scale(ballimg, (30, 30))
ballrect = pg.Rect(400, 450, 30, 30)

vx = random.randint(-10, 10)
vy = -5

replay_img = pg.image.load("images/replaybtn.png")

blocks = []
for yy in range(4):
    for xx in range(7):
        blocks.append(pg.Rect(50 + xx * 100, 40 + yy * 50, 80, 30))

pushFlag = False
page = 1
score = 0


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play()
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


def gamestage():
    global vx, vy
    global page
    global score

    screen.fill(pg.Color("NAVY"))

    (mx, my) = pg.mouse.get_pos()

    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 - 30:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = ((ballrect.x + 15) - (barrect.x + 50)) / 4
        vy = random.randint(-10, -5)
        pg.mixer.Sound("sounds/pi.wav").play()
    if ballrect.y > 600:  #y座標が600超えたらpage2に移って音鳴らす
        page = 2
        pg.mixer.Sound("sounds/down.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

    n = 0
    for block in blocks:
        pg.draw.rect(screen, pg.Color("GOLD"), block)
        if block.colliderect(ballrect):
            pg.mixer.Sound("sounds/piko.wav").play()
            vy = -vy
            blocks[n] = pg.Rect(0, 0, 0, 0)
            score += 1
            if score == 28:
                pg.mixer.Sound("sounds/up.wav").play()
                page = 3
        n += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def gamereset():
    global vx, vy
    global score
    global blocks

    vx = random.randint(-10, 10)  #-10~10までの値の中でランダムに整数を生成
    vy = -5
    ballrect.x = 400
    ballrect.y = 450
    score = 0
    blocks = []
    for yy in range(4):
        for xx in range(7):
            blocks.append(pg.Rect(xx * 100 + 50, yy * 50 + 40, 80, 30))


def gameover():  #ゲームオーバー関数
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("RED"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


while True:
    if page == 1:
        gamestage()
    elif page == 2:  #page2の時はgameover()関数を用いる
        gameover()
    elif page == 3:
        gameclear()

    pg.display.update()
    pg.time.Clock().tick(60)

#イベント終了の決まり文句
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()