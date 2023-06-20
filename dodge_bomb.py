import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0)}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bonb = pg.Surface((20,20))# 練習1
    pg.draw.circle(bonb,(255,0,0),(10,10),10)# 練習1
    bonb.set_colorkey((0,0,0))# 黒い部分を透明にする
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bonb_rect = bonb.get_rect()# 爆弾Surface（bonb_img）から爆弾Rect（bonb_rect）を抽出する
    bonb_rect.center = x , y#中心座標を生成しておいた乱数にする
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()# こうかとんSurface（kk_img）からこうかとんRect（kk_rect）を抽出する
    kk_rect.center = 900,400
    clock = pg.time.Clock()
    tmr = 0
    vx = +5# 練習2
    vy = +5# 練習2
    while True:
        def out_window(rect):
            """
            • 引数：こうかとんRect or 爆弾Rect
            • 戻り値：横方向・縦方向の真理値タプル（True：画面内／False：画面外）
            • Rectオブジェクトのleft, right, top, bottomの値から画面内・外を判断する
            """
            vertical,side = True,True
            if rect.left < 0 or WIDTH <rect.right:
                vertical = False
            if rect.top < 0 or HEIGHT < rect.bottom:
                side = False
            return vertical,side
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        key_lst = pg.key.get_pressed()
        total_move = [0,0]# 合計移動量
        for k,mv in delta.items():
            if key_lst[k]:#辞書によって移動量を変更する 
                total_move[0] += mv[0]
                total_move[1] += mv[1]
        kk_rect.move_ip(total_move)
        if not out_window(kk_rect)[0] or not out_window(kk_rect)[1]:# 練習4
            kk_rect.move_ip(-total_move[0],-total_move[1])#マイナスした座標に移動することでプラスマイナス0にする
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bonb_rect.move_ip(vx,vy)# 練習2
        if not out_window(bonb_rect)[0]:# 練習4
            vx *= -1# 移動方向を反転させる
        elif not out_window(bonb_rect)[1]:#練習4
            vy *= -1
        screen.blit(bonb,bonb_rect)# 練習1
        if kk_rect.colliderect(bonb_rect):#こうかとんと爆弾が衝突したら
            return
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()