import sys
import pygame
import random


from sprite import *
from pygame.sprite import Group
def date_read():
    fd_1 = open("data.txt","r")
    best_score = fd_1.read()
    fd_1.close()
    return best_score
def update_screen(screen,swk,arrows,energy):

    # swk.update()
    swk.blitme(screen,energy)
    for arrow in arrows.sprites():

        arrow.blitme()
    arrows.update()
    # print(len(arrows))
    for arrow in arrows.copy():

        if arrow.rect.left > 954:
            arrows.remove(arrow)
    #         print(len(arrows))
# def update_screen(swk,fruit):
#     swk.blitme()
#     for fruit in fruit.sprites():
#         fruit.draw_fruit()
# def demo():

def add_dragon(screen,dragons):
    e1=Dragon(screen)
    dragons.add(e1)
    # print(len(dragons))
def add_fruit(screen,fruits):
    for i in range(random.randint(1,5)):
        f1=Fruit(screen)
        fruits.add(f1)
def update_f1(screen,fruits):
    for fruit in fruits.sprites():
        fruit.blitme()
        # print(fruit.rect.height)
    # print(len(fruits))

    fruits.update()
    for fruit in fruits.copy():
        if fruit.rect.right<0:
            fruits.remove(fruit)


def update_e1(screen,dragons):
    for dragon in dragons.sprites():
        dragon.blitme()

    dragons.update()
    for dragon in dragons.copy():
        if dragon.rect.right<0:
            dragons.remove(dragon)
    # print(len(dragons))

    # print("dingshangqul")
def collide(swk,arrows,dragons,fruits,score,energy):

    pygame.sprite.groupcollide(arrows, dragons, True, True)
    sprite_list=pygame.sprite.spritecollide(swk,fruits,True)
    score+=len(sprite_list)
    if pygame.sprite.spritecollide(swk,dragons,True):
        print ('碰上了')
        swk.rect.centerx-=10
        energy-=0.25
    return energy,score
        # distroy.image.position=swk.rect.centerx,swk.rect.centery

    # if len(crushs)>0:
    #     die=die+1

# def power():
def v(v0):
    v0-=0.6



def show_score(screen):
    pass
def set_time_passed(screen,clock):
    # 控制画的帧，越大越快
# 得到上一次画图到现在的时间，ms
    time_pass=clock.tick()
def draw_background(screen):
    pass
def create_stones(screen):
    pass
# def draw_stones(screen,stones):
#     # 绘制石头到屏幕，清理跑出去的石头
#     while True:
#         t=random.randint(1,3)
#         sum = random.randint(1, 6)
#
#         if len(stones) < sum:
#             new_stone = Stone(screen)
#             stones.add(new_stone)
#         for stone in stones.copy():
#             stones.update()
#             if stone.rect.right <= 0:
#                 stone.blitme()
#         time.sleep(t)
def update_stones(stones):
    stones.update()
    for stone in stones:
        if stone.rect.right<=0:
            stones.remove(stone)
    print(len(stones))
def create_fruits(screen,fruits):
    # fruits.update()
    while True:
        t = random.randint(1, 6)
        sum=random.randint(1,5)
        if len(fruits)<sum:
            new_fruit=Fruit(screen)
            fruits.add(new_fruit)
        for fruit in fruits.copy():
            fruits.update()
            if fruit.rect.right <= 0:
                fruit.blitme()


        time.sleep(t)

def swk_and_stone_crush(swk,dragon):
    # 检测孙悟空是否撞到石头
    pass
# def swk_eat_fruit(swk,fruits):
#     if

    # 检测孙悟空是否吃到水果
    pass
def draw_swk(screen,swk):
    pass
def game_over(score,screen,font):
    score_text = font.render("Score: " + str(score), 1, (0, 0, 0))
    screen.blit(score_text, [10, 10])
    # while True:
        # 绘制背景图
    pass
