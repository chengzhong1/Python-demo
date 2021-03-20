import pygame
import sys, time, random, math, pygame
from pygame.locals import *
import gf
from sprite import *
import os
# def obstacle(score):
#     probability=1/(1+math.exp(-score))
#     return

def run_game():
    # 初始化
    pygame.init()
    # bg_color = (155, 155, 255)
    screen = pygame.display.set_mode((954,536))

    pygame.display.set_caption("孙悟空快跑！")
    # upImageFilename = 'game_start_up.png'
    # downImageFilename = 'game_start_down.png'
    # button = Button(upImageFilename, downImageFilename, (477, 268))
    # framerate = pygame.time.Clock()
    # screen.fill(bg_color)
    score=0
    die=0
    font=pygame.font.SysFont('方正舒体',30)
    clock=pygame.time.Clock()
    player_jumping = False
    # 实例化
    swk = Swk(screen)
    # my_map=MyMap(screen)

    # fruit=Fruit(screen)
    # arrow=Arrow(screen)
    # stone=Stone(screen)
    # 定义一些变量
    # arrow_vel = 10.0
    # game_over = False
    # you_win = False

    # jump_vel = 0.0
    # player_start_y = player.Y
    # player_hit = False
    # monster_hit = False
    # p_first = True
    # m_first = True
    # best_score = 0
    # 精灵们

    # explosions=Group()
    fruits = Group()
    stones=Group()
    game_pause = True
    index = 0

    score = 0
    replay_flag = True
    # 循环
    bg1 = MyMap(0, 0)
    bg2 = MyMap(954, 0)
    # best_score = gf.data_read()
    t0=time.time()
 
    while game_pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # screen.fill(bg_color)
        # button.render(screen)
        # button.is_start()
        # if button.is_start():
            # 如果孙悟空撞上了石头，游戏结束，调用game_over函数

            # 检测监听事件，空格表示上跳
            # 执行更新函数，改变孙悟空的位置
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        elif keys[K_SPACE]:
            if len(stones)<random.randint(5):
                new_stone=Stone(screen)
                stones.add(new_stone)
            if not player_jumping:
                swk.jump(player_jumping,time_passed)
                gf.suk.update()
                player_jumping = True
                time_passed = time.time() - t0
                t0 = time.time()
                # jump_vel = -12.0
        # 石头与孙悟空的碰撞检测
        if pygame.sprite.spritecollide(swk,stones,False,pygame.sprite.collide_mask):
            distroy.position=swk.centerX.x+50,swk.centerY+50
            die+=1
            # button.game_start=False
            game_pause=False
            # if die>=3:
            #     game_over()

        # gf.swk_and_stone_crush()
        # 孙悟空与水果的碰撞检测
        if pygame.sprite.spritecollide(swk, fruits, True):
            score+=1


        # gf.swk_eat_fruit()
        # # 绘制背景图片
        # gf.draw_background()
        # 显示分数
        # gf.show_score()
        # 生成并绘制石头和水果
        gf.create_fruits(screen,fruits)
        # gf.create_stones(screen,stones)
        swk.reset()


        # 绘制孙悟空
        # swk.jump(player_jumping)

        bg1.map_update()
        bg2.map_update()
        bg1.map_rolling()
        bg2.map_rolling()
        swk.update()
        gf.update_stones(stones)
        # gf.update_screen()
        # pygame.display.update()

        pygame.display.flip()
        clock.tick(60)
    gf.game_over(score,screen,font)

run_game()