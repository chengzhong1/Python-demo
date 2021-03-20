import pygame
import sys
import gf
import re
import serial
import time

from sprite import *
from pygame.locals import *
from pygame.sprite import Group
Background=(250,250,250)
Width=954
Height=536


def ma():

    pygame.init()
    CREACT = pygame.USEREVENT
    screen=pygame.display.set_mode((Width,Height),0,32)
    pygame.display.set_caption("孙悟空快跑")
    clock=pygame.time.Clock()
    running=True
    arrows = Group()
    dragons=Group()
    fruits=Group()
    fires=Group()

    gf.add_dragon(screen,dragons)
    score=0
    background=pygame.image.load("bj.jpg").convert()
    bg1 = MyMap(0, 0)
    bg2 = MyMap(954, 0)
    swk = Swk(screen)
    distroy=Distroy()
    num=0
    gf.add_dragon(screen, dragons)
    pygame.time.set_timer(CREACT, 3000)
    player_jumping=False


    v0=0
    first = swk.screen_rect.centery - 26
    die=0
    energy=1.0
    # ser=serial.Serial("COM4",115200)#实例化串口对象并配置串口基本信息。比如端口号、波特率、最多超时。
    time.sleep(2)
    while running:

        clock.tick(30)
        num=random.randint(0,10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==CREACT:
                if energy<1:
                    energy+=0.01
                if len(fruits)<5:
                    gf.add_fruit(screen,fruits)
                if len(dragons)<3:

                    gf.add_dragon(screen, dragons)

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_b:
                    if score>=5:
                        new_arrow=Arrow(screen,swk)
                        arrows.add(new_arrow)
                        score-=5
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key==pygame.K_SPACE:

                    if swk.rect.centery==first:
                        v0 = -10.0
                        print('在地面')
                        player_jumping=True
                    

        v0+=0.25
        # data = ser.readline()[0:2]#读取串口数据
        # r = str(data)
        # st = re.sub("\D", "", r)#用正则表达式提取串口数据中的数字
        # # s = int(st)#将提取的数字强转为整型，然后才能比较

        # s = int(st)
        # print(s)
        # if s<50:#当串口数据低于100时
        #    if swk.rect.centery==first:
        #         v0 = -10.0
        #         print('在地面')
        #         player_jumping=True
    
        if player_jumping:
            swk.centerY+=v0
            swk.rect.centery=int(swk.centerY)
        if swk.rect.centery >= first:
            player_jumping=False
            swk.rect.centery=first
        
        energy,score=gf.collide(swk, arrows, dragons, fruits,score,energy)

        gf.v(v0)
        bg1.map_update(screen)
        bg2.map_update(screen)
        bg1.map_rolling()
        bg2.map_rolling()
        font = pygame.font.SysFont('方正舒体', 32)
        text_surface = font.render(u'你的分数：%d' % score, True, (1, 200, 200))
        text_rect = text_surface.get_rect()
        text_rect.left = swk.screen_rect.left
        text_rect.top = swk.screen_rect.top
        screen.blit(text_surface, text_rect)
        gf.update_screen(screen,swk, arrows,energy)
        gf.update_e1(screen,dragons)
        gf.update_f1(screen,fruits)
        if energy<=0:
            running=False
            pygame.QUIT
        if score>200:
            print('you win!')
            tex= font.render(u'恭喜你赢了！', True, (250, 100, 100))
            tex_rect = text_surface.get_rect()
            tex_rect.centerx = swk.screen_rect.centerx
            tex_rect.top = swk.screen_rect.top
            screen.blit(tex, tex_rect)
        # data = ser.readline()[0:1]#读取串口数据
        # r = str(data)
        # st = re.sub("\D", "", r)#用正则表达式提取串口数据中的数字
        # # s = int(st)#将提取的数字强转为整型，然后才能比较

        # s = int(st)
        # print(s)
        # if s<5:#当串口数据低于100时
        #    if swk.rect.centery==first:
        #         v0 = -10.0
        #         print('在地面')
        #         player_jumping=True
        # print(score)
        pygame.display.flip()
ma()