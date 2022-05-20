import pygame as pg
import sys
import random
import math
# import sys

pg.init()
screen = pg.display.set_mode((800, 600)) #画面セット

# background = pg.image.load("background.png").convert_alpha() #背景画像の取得
# rect_bg = background.get_rect()

myimgR = pg.image.load("images/you.png")
myimgR = pg.transform.scale(myimgR, (40, 40))
myrect = pg.Rect(50, 200, 40, 50)

walls = [pg.Rect(0, 0, 800, 10),
         pg.Rect(0, 0, 10, 600),
         pg.Rect(780, 0, 10, 600),
         pg.Rect(0, 580, 800, 10)] # 4方向に壁を作る処理

for wall in walls:  # 4つの壁をfor文使って書いてる そのまま使う
    pg.draw.rect(screen, pg.Color("LAVENDERBLUSH"), wall)

foodimg = pg.image.load("images/food.png")
foodimg = pg.transform.scale(foodimg, (30, 30))
foods = []

for i in range(40):  # foodを入れる型を作った
    wx = random.randint(10, 770)
    wy = random.randint(10, 550)
    foods.append(pg.Rect(wx, wy, 30, 30)) # x座標、y座標、大きさ、大きさ
    # print(foods)

replay_img = pg.image.load("images/replaybtn.png")
goalrect = pg.Rect(750, 250, 30, 100)

pushFlag = False
page = 1

#enemy1
enemyimgR = pg.image.load("images/enemy.png")  # enemyの読み込み
enemyimgR = pg.transform.scale(enemyimgR, (50, 50))
#enemyimgL = pg.transform.flip(enemyimgR, True, False)
enemyrect = pg.Rect(700, 0, 50, 50)

# enemy2の追加
enemyimgRR = pg.image.load("images/enemy2.png")  # enemy2の読み込み
enemyimgRR = pg.transform.scale(enemyimgRR, (50, 50))
#enemyimgLL = pg.transform.flip(enemyimgRR, True, False)
enemy2rect = pg.Rect(700, 500, 50, 50)  # x,y座標

def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play()  # 音が鳴る処理
            page = newpage
    else:
        pushFlag = False

yoursize=0
enemysize=0
enemy2size=0
def gamestage():
    global rightFlag
    global page, yoursize, enemysize, enemy2size
    screen.fill(pg.Color("BLACK"))
    font = pg.font.Font(None, 30)
    text = font.render("YOU:"+str(yoursize), True, pg.Color("WHITE")) #スコア表示
    text2 = font.render("YOU:300=CLEAR!", True, pg.Color("GOLD")) #クリア条件表示
    screen.blit(text, (350, 0))
    screen.blit(text2, (350, 580))
    #screen.blit(background, rect_bg)
    vx = 0
    vy = 0
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        if (0 <= yoursize and yoursize <= 20):
            vx += 2
        elif (21 <= yoursize and yoursize <= 50):
            vx += 5
        elif (50 <= yoursize and yoursize <= 70):
            vx += 7
        elif (70 < yoursize and yoursize <= 100):
            vx += 10
        else:
            vx += 15
    if key[pg.K_LEFT]:
        if (0 <= yoursize and yoursize <= 20):
            vx -= 2
        elif (21 <= yoursize and yoursize <= 50):
            vx -= 5
        elif (50 <= yoursize and yoursize <= 70):
            vx -= 7
        elif (70 < yoursize and yoursize <= 100):
            vx -= 10
        else:
            vx -= 15
    if key[pg.K_UP]:
        if (0 <= yoursize and yoursize <= 20):
            vy -= 2
        elif (21 <= yoursize and yoursize <= 50):
            vy -= 5
        elif (50 <= yoursize and yoursize <= 70):
            vy -= 7
        elif (70 < yoursize and yoursize <= 100):
            vy -= 10
        else:
            vy -= 15
    if key[pg.K_DOWN]:
        if (0 <= yoursize and yoursize <= 20):
            vy += 2
        elif (21 <= yoursize and yoursize <= 50):
            vy += 5
        elif (50 <= yoursize and yoursize <= 70):
            vy += 7
        elif (70 < yoursize and yoursize <= 100):
            vy += 10
        else:
            vy += 15

    myrect.x = myrect.x +vx
    myrect.y += vy


    if myrect.collidelist(walls) != -1:# 返り値が-1で無い場合は壁と接触しているという判断
        myrect.x -= vx
        myrect.y -= vy

    screen.blit(myimgR, myrect)

    # foodを配置
    for i in range(len(foods)):
        screen.blit(foodimg, foods[i])

    # foodに触れたときの処理
    n = 0
    for food in foods:
        if food.colliderect(myrect):
            yoursize += 2
            pg.mixer.Sound("sounds/pon.wav").play()
            foods[n] = pg.Rect(random.randint(10, 770),random.randint(20, 550), 30, 30) #別座標へ転換する
        if food.colliderect(enemyrect):
            enemysize += 1
            foods[n] = pg.Rect(random.randint(10, 770), random.randint(20, 550), 30, 30)
        if food.colliderect(enemy2rect):
            enemy2size += 2 # enemy2の方が早く太る
            foods[n] = pg.Rect(random.randint(10, 770), random.randint(20, 550), 30, 30)
        n += 1



    # enemyの移動量
    ovx = 0
    ovy = 0
    if enemyrect.x < myrect.x:
        if (0<=enemysize and enemysize <=10):
            ovx = 2  # enemyが移動する処理
        elif (10<enemysize and enemysize <=30):
            ovx = 3
        elif (30<enemysize and enemysize <=50):
            ovx = 7
        elif (50<enemysize):
            ovx = 10
    else:
        if (0<=enemysize and enemysize <=10):
            ovx = -2  # enemyが移動する処理
        elif (10<enemysize and enemysize <=30):
            ovx = -3
        elif (30<enemysize and enemysize <=50):
            ovx = -7
        elif (50<enemysize):
            ovx = -10
    if enemyrect.y < myrect.y:
        if (0<=enemysize and enemysize <=10):
            ovy = 2  # enemyが移動する処理
        elif (10<enemysize and enemysize <=30):
            ovy = 3
        elif (30<enemysize and enemysize <=50):
            ovy = 7
        elif (50<enemysize):
            ovy = 10
    else:
        if (0<=enemysize and enemysize <=10):
            ovy = -2  # enemyが移動する処理
        elif (10<enemysize and enemysize <=30):
            ovy = -3
        elif (30<enemysize and enemysize <=50):
            ovy = -7
        elif (50<enemysize):
            ovy = -10

    # enemyrect.x += ovx # 敵が追いかけてくる処理（自分の位置に移動量を足す）
    # enemyrect.y += ovy
    enemyrect.x += ovx*((math.log(abs(ovx), math.e)/3))# 敵が追いかけてくる処理（自分の位置に移動量を足す）
    enemyrect.y += ovy

    screen.blit(enemyimgR, enemyrect)

    if myrect.colliderect(enemyrect):  # 衝突判定関数（自分と敵が衝突したら音が鳴り、page2へ移動）and enemysize > yoursize
        pg.mixer.Sound("sounds/down.wav").play()
        page = 2

    # enemy2(黒い方)
    ovxx = 0
    ovyy = 0
    if enemy2rect.x < myrect.x:
        if (0<=enemy2size and enemy2size <=10):
            ovxx = 1  # enemyが移動する処理
        elif (10<enemy2size and enemy2size <=30):
            ovxx = 3
        elif (30<enemy2size and enemy2size <=50):
            ovxx = 5
        elif (50<enemy2size):
            ovxx = 7
    else:
        if (0<=enemy2size and enemy2size <=10):
            ovxx = -1  # enemyが移動する処理
        elif (10<enemy2size and enemy2size <=30):
            ovxx = -3
        elif (30<enemy2size and enemy2size <=50):
            ovxx = -5
        elif (50<enemy2size):
            ovxx = -7
    if enemy2rect.y < myrect.y:
        if (0<=enemy2size and enemy2size <=10):
            ovyy = 1  # enemyが移動する処理
        elif (10<enemy2size and enemy2size <=30):
            ovyy = 3
        elif (30<enemy2size and enemy2size <=50):
            ovyy = 5
        elif (50<enemy2size):
            ovyy = 7
    else:
        if (0<=enemy2size and enemy2size <=10):
            ovyy = -1  # enemyが移動する処理
        elif (10<enemy2size and enemy2size <=30):
            ovyy = -3
        elif (30<enemy2size and enemy2size <=50):
            ovyy = -5
        elif (50<enemy2size):
            ovyy = -7
    enemy2rect.x += ovxx  # enemy2が追いかけてくる処理（自分の位置に移動量を足す）
    enemy2rect.y += ovyy

    screen.blit(enemyimgRR, enemy2rect)

    if myrect.colliderect(enemy2rect):  # 衝突判定関数（自分と敵が衝突したら音が鳴り、page2へ移動）and enemy2size > yoursize
        pg.mixer.Sound("sounds/down.wav").play()
        page = 2

    # クリア条件
    if yoursize == 300:
        pg.mixer.Sound("sounds/up.wav").play()
        page = 3

def gamereset():
    myrect.x = 50
    myrect.y = 100
    for d in range(20):
        foods[d].x = random.randint(20, 770)
        foods[d].y = random.randint(20, 150)


def gameover():
    gamereset()
    screen.fill(pg.Color("WHITE"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMEOVER", True, pg.Color("BLACK"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


def gameclear():
    gamereset()
    screen.fill(pg.Color("GOLD"))
    font = pg.font.Font(None, 150)
    text = font.render("GAMECLEAR", True, pg.Color("BLACK"))
    screen.blit(text, (60, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)


# def food_producer():
#     foods =[]
#     for i in range(40):  # foodをこの個数分出す
#         wx = random.randint(10, 770)
#         wy = random.randint(10, 550)
#         foods.append(pg.Rect(wx, wy, 30, 30))


while True:
    if page == 1:
        gamestage()  # page1の時はこの画面を出す関数
    elif page == 2:
        yoursize = 0
        enemysize = 0
        enemy2size = 0
        enemyrect = pg.Rect(700, 0, 50, 50)
        enemy2rect = pg.Rect(700, 500, 50, 50)
        gameover()
    elif page == 3:
        yoursize = 0
        enemysize = 0
        enemy2size = 0
        enemyrect = pg.Rect(700, 0, 50, 50)
        enemy2rect = pg.Rect(700, 500, 50, 50)
        gameclear()

    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
