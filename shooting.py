### インポート
import sys
import time
import random
import pygame
from pygame.locals import *

### 定数
WIDTH = 400  # 画面横サイズ
HEIGHT = 400  # 画面縦サイズ
BTY_W_SIZE = 50  # 砲台横サイズ
BTY_H_SIZE = 50  # 砲台縦サイズ
BTY_H_POS = 30  # 砲台縦位置
MSL_W_SIZE = 10  # ミサイル横サイズ
MSL_H_SIZE = 10  # ミサイル縦サイズ
ENY_W_SIZE = 30  # エネミー横サイズ
ENY_H_SIZE = 10  # エネミー縦サイズ
MSL_SPD = 20  # ミサイル移動速度
ENY_H_POS = 20  # エネミー縦位置
F_RATE = 30  # フレームレート
W_TIME = 30  # 待ち時間
FONT_SIZE = 50  # フォントサイズ
MES_TIME = 400  # メッセージ表示時間

### 画面定義(X軸,Y軸,横,縦)
SURFACE = Rect(0, 0, WIDTH, HEIGHT)


############################
### 砲台クラス
############################
class Battery(pygame.sprite.Sprite):

    ############################
    ### 初期化メソッド
    ############################
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        self.image = pygame.image.load(name).convert_alpha()

        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (BTY_W_SIZE, BTY_H_SIZE))

        ### 砲台オブジェクト生成
        self.rect = self.image.get_rect()

        ### 砲台位置
        self.rect.centerx = int(SURFACE.width / 2)
        self.rect.centery = SURFACE.bottom - BTY_H_POS

    ############################
    ### 砲台描画
    ############################
    def draw(self, surface):
        surface.blit(self.image, self.rect)


############################
### ミサイルクラス
############################
class Missile(pygame.sprite.Sprite):

    ############################
    ### 初期化メソッド
    ############################
    def __init__(self, name, battery, enemies):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        self.image = pygame.image.load(name).convert()

        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (MSL_W_SIZE, MSL_H_SIZE))

        ### ミサイルオブジェクト生成
        self.rect = self.image.get_rect()

        ### 他オブジェクト保存
        self.battery = battery
        self.enemy = enemies

        ### ミサイル初期位置
        self.rect.centerx = self.battery.rect.centerx
        self.rect.bottom = self.battery.rect.top

    ############################
    ### ミサイル移動
    ############################
    def update(self, surface):

        ### ミサイル速度
        self.rect.centery -= MSL_SPD

        ### 命中判定
        enemy_list = pygame.sprite.spritecollide(self, self.enemy, True)

        ### 命中した場合、画面にHITを表示
        if len(enemy_list) > 0:
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render("HIT", True, (96, 255, 96))
            surface.blit(text, [171, 182])
            pygame.display.update()
            pygame.time.wait(MES_TIME)

        ### 命中したか画面外に出た場合、ミサイルを消去
        if len(enemy_list) > 0 or self.rect.top < 0:
            self.kill()


############################
### エネミークラス
############################
class Enemy(pygame.sprite.Sprite):

    ############################
    ### 初期化メソッド
    ############################
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        self.image = pygame.image.load(name).convert()

        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (ENY_W_SIZE, ENY_H_SIZE))

        ### エネミーオブジェクト生成
        self.rect = self.image.get_rect()

        ### エネミー初期位置
        self.rect.left = 0
        self.rect.top = ENY_H_POS

    ############################
    ### エネミー移動
    ############################
    def update(self):
        ### エネミー速度
        self.rect.centerx += random.randint(6, 10)

        ### 画面外に出たら消去
        if self.rect.left > SURFACE.width:
            self.kill()


############################
### メイン関数
############################
def main():
    ### 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)

    ### 砲台作成
    battery = Battery("battery.png")

    ### ミサイルグループ
    missiles = pygame.sprite.Group()

    ### エネミーグループ
    enemies = pygame.sprite.Group()

    ### 時間オブジェクト生成
    clock = pygame.time.Clock()

    ### 無限ループ
    while True:

        ### フレームレート設定
        clock.tick(F_RATE)

        ### 背景色設定
        surface.fill((0, 0, 0))

        ### エネミー出現
        if len(enemies) == 0:
            if random.randint(0, 20) > 19:
                enemies.add(Enemy("enemy.png"))

        ### スプライトを更新
        missiles.update(surface)
        enemies.update()

        ### スプライトを描画
        battery.draw(surface)
        missiles.draw(surface)
        enemies.draw(surface)

        ### 画面更新
        pygame.display.update()
        pygame.time.wait(W_TIME)

        ### イベント処理
        for event in pygame.event.get():

            ### 終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()

                ### ミサイル発射
                if event.key == K_SPACE:
                    missiles.add(Missile("missile.png", battery, enemies))


############################
### 終了関数
############################
def exit():
    pygame.quit()
    sys.exit()


############################
### メイン関数呼び出し
############################
if __name__ == "__main__":
    ### 処理開始
    main()