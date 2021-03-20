
from pygame.locals import *
from MyLibrary import *
from sprite import *





while True:
    framerate.tick(60)
    ticks = pygame.time.get_ticks()


    button.render(screen)
    button.is_start()
    if button.game_start == True:
        if game_pause :
        # if True:
            start_time = time.time()
            index +=1
            tmp_x =0
            if score >int (best_score):
                best_score = score
            fd_2 = open("data.txt","w+")
            fd_2.write(str(best_score))
            fd_2.close()
            #判断游戏是否通关
            if index == 0:
                you_win = True
            if you_win:
                screen.fill((200, 200, 200))
                print_text(font1, 270, 150,"YOU WIN THE GAME!",(240,20,20))
                current_time =time.time()-start_time
                print_text(font1, 320, 250, "Best Score:",(120,224,22))
                print_text(font1, 370, 290, str(best_score),(255,0,0))
                print_text(font1, 270, 330, "This Game Score:",(120,224,22))
                print_text(font1, 385, 380, str(score),(255,0,0))
                pygame.display.update()
                pygame.quit()
                sys.exit()
                
            for i in range(0,100):
                element = MySprite()
                element.load("fruit.bmp", 75, 20, 1)
                tmp_x +=random.randint(50,120)
                element.X = tmp_x+300
                element.Y = random.randint(80,200)
                group_fruit.add(element)
            

            #更新子弹
            if not game_over:
                arrow.X -= arrow_vel
            if arrow.X < -40: reset_arrow()
            #碰撞检测，子弹是否击中玩家
            if pygame.sprite.collide_rect(arrow, player):
                reset_arrow()
                explosion.position =player.X,player.Y
                player_hit = True
                # hit_sound.play_sound()
                if p_first:
                    group_exp.add(explosion)
                    p_first = False
                player.X -= 10

            #碰撞检测，子弹是否击中怪物
            if pygame.sprite.collide_rect(arrow, dragon):
                reset_arrow()
                explosion.position =dragon.X+50,dragon.Y+50
                monster_hit = True
                # hit_sound.play_sound()
                if m_first:
                    group_exp.add(explosion)
                    m_first = False
                dragon.X -= 10

            #碰撞检测，玩家是否被怪物追上
            if pygame.sprite.collide_rect(player, dragon):
                game_over = True
            #遍历果实，使果实移动
            for e in group_fruit:
                e.X -=5
            collide_list = pygame.sprite.spritecollide(player,group_fruit,False)
            score +=len(collide_list)
            #是否通过关卡
            if dragon.X < -100:
                game_pause = True
                reset_arrow()
                player.X = 400
                dragon.X = 100
                
            

            #检测玩家是否处于跳跃状态



            #绘制背景

            
            #更新精灵组
            if not game_over:
                group.update(ticks, 60)
                group_exp.update(ticks,60)
                group_fruit.update(ticks,60)

                replay_flag =False
            #绘制精灵组
            group.draw(screen)
            group_fruit.draw(screen)
            if player_hit or monster_hit:
                group_exp.draw(screen)
            print_text(font, 330, 560, "press SPACE to jump up!")
            print_text(font, 200, 20, "You have get Score:",(219,224,22))
            print_text(font1, 380, 10, str(score),(255,0,0))
            if game_over:
                start_time = time.clock()
                current_time =time.clock()-start_time
                while current_time<500:
                    screen.fill((200, 200, 200))
                    print_text(font1, 300, 150,"GAME OVER!",(240,20,20))
                    current_time =time.clock()-start_time
                    print_text(font1, 320, 250, "Best Score:",(120,224,22))
                    if score >int (best_score):
                        best_score = score
                    print_text(font1, 370, 290, str(best_score),(255,0,0))
                    print_text(font1, 270, 330, "This Game Score:",(120,224,22))
                    print_text(font1, 370, 380, str(score),(255,0,0))
                    pygame.display.update()
                fd_2 = open("data.txt","w+")
                fd_2.write(str(best_score))
                fd_2.close()
                pygame.quit()
                sys.exit()
    pygame.display.update()
