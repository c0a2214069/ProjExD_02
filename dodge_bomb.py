import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bonb = pg.Surface((20,20))# 練習1
    pg.draw.circle(bonb,(255,0,0),(10,10),10)# 練習1
    bonb.set_colorkey((0,0,0))
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bonb_rect = bonb.get_rect()
    bonb_rect.center = x , y
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    vx = +5# 練習2
    vy = +5# 練習2
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        key_lst = pg.key.get_pressed()
        print(key_lst)
        bonb_rect.move_ip(vx,vy)
        screen.blit(bonb,bonb_rect)# 練習1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()