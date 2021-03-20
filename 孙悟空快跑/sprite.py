from MyLibrary import *
from pygame.sprite import Sprite
from pygame.sprite import Group
import pygame


# arrow.load("flame.png", 40, 16, 1)
# arrow.position = 800,320
# group.add(arrow)
# #重置火箭函数
class Fire(Sprite):
    def __init__(self,screen,dragon):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('flame.png')
        self.rect = self.image.get_rect()


        self.rect.right=dragon.rect.left
        self.rect.centery=dragon.rect.centery
        self.x=self.rect.centerx
    def update(self):
        self.x-=3
        self.rect.centerx=self.x
    def blitme(self):
        self.screen.blit(self.image,self.rect)
class Arrow(Sprite):
    def __init__(self,screen,swk):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('blue.png')
        self.rect = self.image.get_rect()


        self.rect.left=swk.rect.right
        self.rect.centery=swk.rect.centery
        self.x=self.rect.centerx
    def update(self):
        self.x+=3
        self.rect.centerx=self.x
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    # def reset_arrow(self):
    #     y = random.randint(270,350)
    #     self.x,self.y = 800,y
    #
    #
    #
    #     # 创建地图对象
class Fruit(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('fruit.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # self.rect.top=random.randrange(self.screen_rect.top-5*self.rect.height,self.screen_rect.top-2*self.rect.height,self.rect.height)
        # self.rect.left=random.randrange(self.screen_rect.right,self.screen_rect.right+5*self.rect.width,self.rect.width)
        self.rect.top=self.screen_rect.top+random.randrange(2*self.rect.height,5*self.rect.height,self.rect.height)
        self.rect.left=self.screen_rect.right+random.randrange(0,4*self.rect.width,self.rect.width)





    # 不断向左移动
    def update(self):
        self.x=float(self.rect.centerx)
        self.x-=6
        self.rect.centerx=self.x

    # 把水果画上去
    def blitme(self):
        self.screen.blit(self.image,self.rect)
class Dragon(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('dragon1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery-10
        self.rect.right = random.randrange(self.screen_rect.right,self.screen_rect.right+5*self.rect.width,self.rect.width)
        self.mask=pygame.mask.from_surface(self.image)
        # 不断向左移动

    def update(self):
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.x -= 6

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)



class Distroy(Sprite):
    def __init__(self):
        super().__init__()
        # self.image=pygame.image.load("explosion.png", 128, 128, 6)




class Swk(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('qiqi.png')
        self.screen_rect = screen.get_rect()
        self.rect=self.image.get_rect()
        self.rect.centerx = (2/3)*self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery-26
        self.centerX=float(self.rect.centerx)
        self.centerY=float(self.rect.centery)
        # self.mask = pygame.mask.from_surface(self.image)
        # self.blitme()
        # self.screen.x=self.screen_rect.

    def blitme(self,screen,energy):
        self.screen.blit(self.image,self.rect)

        pygame.draw.line(screen,(0,0,0),(self.rect.left,self.rect.top-5),(self.rect.right,self.rect.top-5),4)
        if energy>0.3:
            energy_color=(0,255,0)
        else:
            energy_color=(255,0,0)
        pygame.draw.line(screen,energy_color,(self.rect.left,self.rect.top-5),(self.rect.left+self.rect.width*energy,\
                                                                               self.rect.top-5),4)



    # def reset(self):
    #
    #     self.is_jumping = False
    #     # 恐龙是否在向上跳跃
    #     self.player_jumping = True
    #     # 跳跃初始速度
    #     self.jump_v0 = 500
    #     # 跳跃瞬时速度
    #     self.jump_v = self.jump_v0
    #     # 跳跃加速度
    #     self.jump_a_up = 1000
    #     self.jump_a_down = 800
    #     # 小恐龙初始位置
    #     self.initial_left = 40
    #     self.initial_top = int(500/ 2.3)
    #
    #     self.image = self.image.subsurface((0, 0), (98, 121))
    #     self.rect = self.image.get_rect()
    #     self.rect.left, self.rect.top = self.initial_left, self.initial_top
    #

# class Gravity():
#     def __init__(self):
#         space=pymunk.Space()
#         space.gravity=(0.0,-900)
#         static_body=space.static_body
#         static_lines=[]



#创建爆炸动画
# explosion = MySprite()
# explosion.load("explosion.png",128,128,6)
#创建玩家精灵
# player = MySprite()
# player.load("qiqi.png", 98, 121, 1)
# player.position = 400, 270
# # group.add(player)












# 定义一个按钮类
class Button(object):
    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.game_start = False

    def isOver(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self,screen):
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            screen.blit(self.imageDown, (x - w / 2, y - h / 2))
        else:
            screen.blit(self.imageUp, (x - w / 2, y - h / 2))

    def is_start(self):
        if self.isOver():
            b1, b2, b3 = pygame.mouse.get_pressed()
            if b1 == 1:
                return True
class MyMap(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bg = pygame.image.load("bj.jpg")

    def map_rolling(self):
        if self.x < -954:
            self.x = 954
        else:
            self.x -= 6

    def map_update(self,screen):
        screen.blit(self.bg, (self.x, self.y))

    def set_pos(self, x, y):
        self.x = x
        self.y = y


