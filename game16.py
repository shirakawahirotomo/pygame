##敵キャラに当たり判定あり
##効果音が流れる
##お化けが追いかけてくる


import pygame as pg, sys
import random 
pg.init()
screen = pg.display.set_mode((800, 600))

myimgR = pg.image.load("images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myrect = pg.Rect(50, 200, 40, 50)


walls = [pg.Rect(0, 0, 800, 20),
         pg.Rect(0, 0, 20, 600),
         pg.Rect(780, 0, 20, 600),
         pg.Rect(0, 580, 800, 20)] ##4方向に壁を作る処理

trapimg = pg.image.load("images/uni.png")
trapimg = pg.transform.scale(trapimg, (30, 30))
traps = []
for i in range(40):#うにをこの個数分出す?
    wx = 150 + i * 30
    wy = random.randint(20, 550)
    traps.append(pg.Rect(wx, wy, 30, 30))

replay_img = pg.image.load("images/replaybtn.png")
goalrect = pg.Rect(750, 250, 30, 100)

rightFlag = True
pushFlag = False
page = 1

enemyimgR = pg.image.load("images/obake.png")##おばけの追加
enemyimgR = pg.transform.scale(enemyimgR, (50, 50))
enemyimgL = pg.transform.flip(enemyimgR, True, False)
enemyrect = pg.Rect(650, 200, 50, 50)

###キャラ2体目
enemyimgRR = pg.image.load("images/kaeru.png")##2体目キャラの追加
enemyimgRR = pg.transform.scale(enemyimgRR, (50, 50))
enemyimgLL = pg.transform.flip(enemyimgRR, True, False)
enemy2rect = pg.Rect(300, 100, 50, 50)##x,y座標


def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play() ##音が鳴る処理 
            page = newpage
    else:
        pushFlag = False
def gamestage():
    global rightFlag
    global page
    screen.fill(pg.Color("DEEPSKYBLUE"))
    vx = 0
    vy = 0
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        vx += 10
        rightFlag = True
    if key[pg.K_LEFT]:
        vx += -10
        rightFlag = False
    if key[pg.K_UP]:
        vy += -10
    if key[pg.K_DOWN]:
        vy += 10

    myrect.x += vx
    myrect.y += vy

    if myrect.collidelist(walls) != -1:##返り値が-1で無い場合は壁と接触しているという判断
        myrect.x -= vx
        myrect.y -= vy

    if rightFlag:
        screen.blit(myimgR, myrect)
    else:
        screen.blit(myimgL, myrect)
    
    for wall in walls:##4つの壁をfor文使って書いてる
        pg.draw.rect(screen, pg.Color("DARKGREEN"), wall)

    for trap in traps:
        screen.blit(trapimg, trap)
    if myrect.collidelist(traps) != -1:
        pg.mixer.Sound("sounds/down.wav").play() ##
        page = 2

    pg.draw.rect(screen, pg.Color("GOLD"), goalrect) ##goalrectでゴールの表示している
    if myrect.colliderect(goalrect):##goalrectとmyrectが重なったらpage3に飛んで音が鳴る処理
        pg.mixer.Sound("sounds/up.wav").play()
        page = 3

    # ovx = 0 ##おばけの移動量 加速度の処理追加してみたら？
    ovy = 0
    if enemyrect.x < myrect.x:
        ovx = 1 ##おばけが移動する処理
    else:
        ovx = -1
    if enemyrect.y < myrect.y:
        ovy = 1
    else:
        ovy = -1
    enemyrect.x += ovx ##おばけが追いかけてくる処理（自分の位置に移動量を足す）
    enemyrect.y += ovy
    if ovx > 0:
        screen.blit(enemyimgR, enemyrect)
    else:
        screen.blit(enemyimgL, enemyrect)
    if myrect.colliderect(enemyrect):##衝突判定関数（自分のキャラと敵キャラが衝突したら音が鳴り、page2へ移動）
        pg.mixer.Sound("sounds/down.wav").play()
        page = 2

    ###キャラ2体目
    ovxx = 0
    ovyy = 0

    if enemy2rect.x < myrect.x:
        ovxx = 1 ##キャラが移動する処理
    else:
        ovxx = -1
    if enemy2rect.y < myrect.y:
        ovyy = 1
    else:
        ovyy = -1
    enemy2rect.x += ovxx ##キャラが追いかけてくる処理（自分の位置に移動量を足す）
    enemy2rect.y += ovyy
    if ovxx > 0:
        screen.blit(enemyimgRR, enemy2rect)
    else:
        screen.blit(enemyimgLL, enemy2rect)
    if myrect.colliderect(enemy2rect):##衝突判定関数（自分のキャラと敵キャラが衝突したら音が鳴り、page2へ移動）
        pg.mixer.Sound("sounds/down.wav").play()
        page = 2

def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        traps[d].x = 150 + d * 30
        traps[d].y= random.randint(20, 150)

def gameover():
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
        gamestage()##page1の時はこの画面を出す関数
    elif page == 2:
        gameover()
    elif page == 3:
        gameclear()
 
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
