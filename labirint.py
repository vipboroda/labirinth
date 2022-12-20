from pygame import * 
from pygame import mixer
init() 
mw = display.set_mode((768, 768)) 
mw.fill((150, 200, 100)) 
display.set_caption('Лабиринт') 
run = True 
finish = False
picture = transform.scale(image.load('fon.png'), (768, 768))
surf = Surface((768, 768))
mixer.music.load('back.mp3')
mixer.music.play(-1)

class GameSprite(sprite.Sprite): 
    def __init__(self, pic, x, y, w, h): 
        super().__init__()
        self.image = transform.scale(image.load(pic), (w, h)) 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
    def reset(self): 
        mw.blit(self.image,(self.rect.x, self.rect.y))
        self.rect.clamp_ip(surf.get_rect())            
 
class Hero(GameSprite):
    def __init__(self, pic, x, y, w, h, speed_x, speed_y):
        super().__init__(pic, x, y, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x  
        self.rect.y += self.speed_y
        walls_touch = sprite.spritecollide(self, walls, False)
        for i in walls_touch:
            if self.speed_x > 0:
                self.rect.right = min(self.rect.right, i.rect.left)
            if self.speed_x < 0:
                self.rect.left = max(self.rect.left, i.rect.right)
            elif self.speed_y > 0:
                self.rect.bottom = min(self.rect.bottom, i.rect.top)
            elif self.speed_y < 0:
                self.rect.top = max(self.rect.top, i.rect.bottom)
    def fire(self): 
        throw_sound = mixer.Sound('throw.wav')
        throw_sound.play()
        bullets.add(Bullet('shuriken.png', self.rect.right, self.rect.centery, 10, 10))


class Enemy(GameSprite):
    def __init__(self, pic, x, y, w, h, y1, y2, speed):
        super().__init__(pic, x, y, w, h)
        self.direction = 'bottom'
        self.speed = speed
        self.y1 = y1
        self.y2 = y2
    def update(self):
        if self.rect.y >= self.y1:
            self.direction = 'bottom'
        elif self.rect.y <= self.y2:
            self.direction = 'top'
        if self.direction == 'bottom':
            self.rect.y -=self.speed
        else:
            self.rect.y += self.speed


class Obstacles(GameSprite):
    def __init__(self, pic, x, y, w, h, x1, x2, speed):
        super().__init__(pic, x, y, w, h)
        self.direction = 'left'
        self.speed = speed
        self.x1 = x1
        self.x2 = x2
    def update(self):
        if self.rect.x >= self.x1:
            self.direction = 'left'
        elif self.rect.x <= self.x2:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -=self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite): 
    def __init__(self, pic, x, y, w, h, speed=6): 
        super().__init__(pic, x, y, w, h) 
        self.speed = speed 
    def update(self): 
        self.rect.x += self.speed 
        if self.rect.x >= 768: 
            self.kill() 
        
        
walls = sprite.Group()
walls.add(GameSprite('wall2.png', 0, 668, 50, 50))
walls.add(GameSprite('wall2.png', 0, 718, 50, 50))
walls.add(GameSprite('wall2.png', 50, 718, 50, 50))
walls.add(GameSprite('wall2.png', 50, 668, 50, 50))
walls.add(GameSprite('wall2.png', 0, 618, 50, 50))
walls.add(GameSprite('wall2.png', 25, 618, 50, 50))
walls.add(GameSprite('wall2.png', 0, 568, 50, 50))
walls.add(GameSprite('wall2.png', -25, 518, 50, 50))
walls.add(GameSprite('wall2.png', 0, 468, 50, 50))
walls.add(GameSprite('wall2.png', 0, 418, 50, 50))
walls.add(GameSprite('wall2.png', 50, 443, 50, 50))
walls.add(GameSprite('wall2.png', 50, 393, 50, 50))
walls.add(GameSprite('wall2.png', 50, 343, 50, 50))
walls.add(GameSprite('wall2.png', 100, 418, 50, 50))
walls.add(GameSprite('wall2.png', 100, 393, 50, 50))
walls.add(GameSprite('wall2.png', 100, 363, 50, 50))
walls.add(GameSprite('wall2.png', 150, 393, 50, 50))
walls.add(GameSprite('wall2.png', 200, 393, 50, 50))
walls.add(GameSprite('wall2.png', 250, 393, 50, 50))
walls.add(GameSprite('wall2.png', 300, 393, 50, 50))
walls.add(GameSprite('wall2.png', 350, 318, 50, 50))
walls.add(GameSprite('wall2.png', 350, 393, 50, 50))
walls.add(GameSprite('wall2.png', 350, 368, 50, 50))
walls.add(GameSprite('wall2.png', 300, 368, 50, 50))
walls.add(GameSprite('wall2.png', 300, 318, 50, 50))
walls.add(GameSprite('wall2.png', 250, 368, 50, 50))
walls.add(GameSprite('wall2.png', 250, 318, 50, 50))
walls.add(GameSprite('wall2.png', 200, 368, 50, 50))
walls.add(GameSprite('wall2.png', 200, 318, 50, 50))
walls.add(GameSprite('wall2.png', 150, 368, 50, 50))
walls.add(GameSprite('wall2.png', 150, 318, 50, 50))
walls.add(GameSprite('wall2.png', 100, 368, 50, 50))
walls.add(GameSprite('wall2.png', 100, 318, 50, 50))
walls.add(GameSprite('wall2.png', 50, 368, 50, 50))
walls.add(GameSprite('wall2.png', 50, 318, 50, 50))
walls.add(GameSprite('wall2.png', 350, 620, 50, 50))
walls.add(GameSprite('wall2.png', 400, 620, 50, 50))
walls.add(GameSprite('wall2.png', 450, 620, 50, 50))
walls.add(GameSprite('wall2.png', 500, 620, 50, 50))
walls.add(GameSprite('wall2.png', 550, 620, 50, 50))
walls.add(GameSprite('wall2.png', 300, 417, 50, 50))
walls.add(GameSprite('wall2.png', 300, 718, 50, 50))
walls.add(GameSprite('wall2.png', 350, 718, 50, 50))
walls.add(GameSprite('wall2.png', 400, 718, 50, 50))
walls.add(GameSprite('wall2.png', 450, 718, 50, 50))
walls.add(GameSprite('wall2.png', 350, 668, 50, 50))
walls.add(GameSprite('wall2.png', 400, 668, 50, 50))
walls.add(GameSprite('wall2.png', 450, 668, 50, 50))
walls.add(GameSprite('wall2.png', 500, 668, 50, 50))
walls.add(GameSprite('wall2.png', 500, 718, 50, 50))
walls.add(GameSprite('wall2.png', 550, 668, 50, 50))
walls.add(GameSprite('wall2.png', 550, 718, 50, 50))
walls.add(GameSprite('wall2.png', 600, 668, 50, 50))
walls.add(GameSprite('wall2.png', 600, 718, 50, 50))
walls.add(GameSprite('wall2.png', 620, 568, 50, 50))
walls.add(GameSprite('wall2.png', 595, 518, 50, 50))
walls.add(GameSprite('wall2.png', 595, 568, 50, 50))
walls.add(GameSprite('wall2.png', 595, 618, 50, 50))
walls.add(GameSprite('wall2.png', 620, 518, 50, 50))
walls.add(GameSprite('wall2.png', 670, 518, 50, 50))
walls.add(GameSprite('wall2.png', 565, 618, 50, 50))
walls.add(GameSprite('wall2.png', 565, 568, 50, 50))
walls.add(GameSprite('wall2.png', 565, 518, 50, 50))
walls.add(GameSprite('wall2.png', 515, 518, 50, 50))
walls.add(GameSprite('wall2.png', 515, 568, 50, 50))
walls.add(GameSprite('wall2.png', 515, 518, 50, 50))
walls.add(GameSprite('wall2.png', 515, 468, 50, 50))
walls.add(GameSprite('wall2.png', 515, 418, 50, 50))
walls.add(GameSprite('wall2.png', 515, 368, 50, 50))
walls.add(GameSprite('wall2.png', 515, 318, 50, 50))
walls.add(GameSprite('wall2.png', 515, 268, 50, 50))
walls.add(GameSprite('wall2.png', 515, 218, 50, 50))
walls.add(GameSprite('wall2.png', 515, 208, 50, 50))
walls.add(GameSprite('wall2.png', 650, 668, 50, 50))
walls.add(GameSprite('wall2.png', 650, 718, 50, 50))
walls.add(GameSprite('wall2.png', 670, 618, 50, 50))
walls.add(GameSprite('wall2.png', 670, 568, 50, 50))
walls.add(GameSprite('wall2.png', 620, 618, 50, 50))
walls.add(GameSprite('wall2.png', 700, 668, 50, 50))
walls.add(GameSprite('wall2.png', 700, 718, 50, 50))
walls.add(GameSprite('wall2.png', 750, 668, 50, 50))
walls.add(GameSprite('wall2.png', 750, 718, 50, 50))
walls.add(GameSprite('wall2.png', 720, 618, 50, 50))
walls.add(GameSprite('wall2.png', 720, 568, 50, 50))
walls.add(GameSprite('wall2.png', 720, 518, 50, 50))
walls.add(GameSprite('wall2.png', 745, 468, 50, 50))
walls.add(GameSprite('wall2.png', 745, 418, 50, 50))
walls.add(GameSprite('wall2.png', 745, 368, 50, 50))
walls.add(GameSprite('wall2.png', 720, 318, 50, 50))
walls.add(GameSprite('wall2.png', 720, 268, 50, 50))
walls.add(GameSprite('wall2.png', 720, 218, 50, 50))
walls.add(GameSprite('wall2.png', 720, 168, 50, 50))
walls.add(GameSprite('wall2.png', 720, 118, 50, 50))
walls.add(GameSprite('wall2.png', 720, 68, 50, 50))
walls.add(GameSprite('wall2.png', 720, 18, 50, 50))
walls.add(GameSprite('wall2.png', 720, 0, 50, 50))
walls.add(GameSprite('wall2.png', 720, 0, 50, 50))
walls.add(GameSprite('wall2.png', 670, 0, 50, 50))
walls.add(GameSprite('wall2.png', 620, 0, 50, 50))
walls.add(GameSprite('wall2.png', 570, 0, 50, 50))
walls.add(GameSprite('wall2.png', 520, 0, 50, 50))
walls.add(GameSprite('wall2.png', 470, 0, 50, 50))
walls.add(GameSprite('wall2.png', 420, 0, 50, 50))
walls.add(GameSprite('wall2.png', 370, 0, 50, 50))
walls.add(GameSprite('wall2.png', 320, 0, 50, 50))
walls.add(GameSprite('wall2.png', 270, 0, 50, 50))
walls.add(GameSprite('wall2.png', 220, 0, 50, 50))
walls.add(GameSprite('wall2.png', 170, 0, 50, 50))
walls.add(GameSprite('wall2.png', 120, 0, 50, 50))
walls.add(GameSprite('wall2.png', 70, 0, 50, 50))
walls.add(GameSprite('wall2.png', 20, 0, 50, 50))
walls.add(GameSprite('wall2.png', 0, 0, 50, 50))
walls.add(GameSprite('wall2.png', 0, 50, 50, 50))
walls.add(GameSprite('wall2.png', -25, 100, 50, 50))
walls.add(GameSprite('wall2.png', -25, 150, 50, 50))
walls.add(GameSprite('wall2.png', -25, 200, 50, 50))
walls.add(GameSprite('wall2.png', -25, 250, 50, 50))
walls.add(GameSprite('wall2.png', 0, 300, 50, 50))
walls.add(GameSprite('wall2.png', 0, 350, 50, 50))
walls.add(GameSprite('wall2.png', 0, 400, 50, 50))
walls.add(GameSprite('wall2.png', 0, 450, 50, 50))
walls.add(GameSprite('wall2.png', 0, 500, 50, 50))
walls.add(GameSprite('wall2.png', 0, 550, 50, 50))
walls.add(GameSprite('wall2.png', 0, 600, 50, 50))
walls.add(GameSprite('wall2.png', 0, 650, 50, 50))
walls.add(GameSprite('wall2.png', 0, 700, 50, 50))
walls.add(GameSprite('wall2.png', 0, 750, 50, 50))
walls.add(GameSprite('wall2.png', 0, 768, 50, 50))
walls.add(GameSprite('wall2.png', 300, 668, 50, 50))
walls.add(GameSprite('wall2.png', 275, 618, 50, 50))
walls.add(GameSprite('wall2.png', 300, 618, 50, 50))
walls.add(GameSprite('wall2.png', 250, 568, 50, 50))
walls.add(GameSprite('wall2.png', 150, 160, 50, 50))
walls.add(GameSprite('wall2.png', 200, 160, 50, 50))
walls.add(GameSprite('wall2.png', 250, 160, 50, 50))
walls.add(GameSprite('wall2.png', 300, 160, 50, 50))
walls.add(GameSprite('wall2.png', 350, 160, 50, 50))
walls.add(GameSprite('wall2.png', 400, 160, 50, 50))
walls.add(GameSprite('wall2.png', 450, 160, 50, 50))
walls.add(GameSprite('wall2.png', 500, 160, 50, 50))
walls.add(GameSprite('wall2.png', 515, 160, 50, 50))


hero = Hero('right.png', 175, 718, 48, 30, 0, 0) 
#для enemy y1 должен быть больше y2 иначе не будет воркать
enemies = sprite.Group()
enemies.add(Enemy('meduza.png', 358, 580, 30, 45, 570, 450, 1))
enemies.add(Enemy('meduza.png', 400, 120, 30, 45, 120, 50, 1))
enemies.add(Enemy('meduza.png', 300, 100, 30, 45, 120, 50, 1))
enemies.add(Enemy('meduza.png', 200, 80, 30, 45, 120, 50, 1))


obstacles = sprite.Group()
obstacles.add(Obstacles('s.png', 420, 400, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 470, 305, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 120, 600, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 210, 480, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 460, 550, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 115, 70, 30, 30, 0, 0, 0))
obstacles.add(Obstacles('s.png', 650, 65, 60, 60, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 530, 125, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 500, 125, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 470, 125, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 350, 282, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 320, 282, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 290, 282, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 260, 282, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 90, 281, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 60, 281, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 230, 125, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vdown.png', 260, 125, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vup.png', 210, 200, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vup.png', 180, 200, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vup.png', 150, 200, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vup.png', 350, 50, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 25, 250, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 25, 220, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 25, 100, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 566, 200, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 566, 230, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 566, 260, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 566, 290, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vright.png', 566, 320, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vleft.png', 686, 200, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vleft.png', 686, 230, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vleft.png', 686, 260, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vleft.png', 686, 290, 35, 35, 0, 0, 0))
obstacles.add(Obstacles('vleft.png', 686, 320, 35, 35, 0, 0, 0))


bullets = sprite.Group() 
goal = GameSprite('computer.png', 695, 440, 35, 75)
win = GameSprite('win.png', 250, 380, 300, 80)
loose = GameSprite('loose.png', 250, 380, 300, 80)

while run: 
    time.delay(10) 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
        elif e.type == KEYDOWN:
            if e.key == K_w:
                hero.speed_y = -2
            elif e.key == K_s:
                hero.speed_y = 2
            elif e.key == K_a:
                hero.speed_x = -2
                
            elif e.key == K_d:
                hero.speed_x = 2
                
            elif e.key == K_SPACE: 
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_w:
                hero.speed_y = 0
            elif e.key == K_s:
                hero.speed_y = 0
            elif e.key == K_a:
                hero.speed_x = 0
                
            elif e.key == K_d:
                hero.speed_x = 0
                
    if finish != True:
        mw.blit(picture, (0, 0))
        hero.reset()
        hero.update()
        enemies.draw(mw)
        enemies.update()
        obstacles.draw(mw)
        obstacles.update()
        goal.reset()
        walls.draw(mw)
        bullets.draw(mw) 
        bullets.update() 
        if sprite.collide_rect(hero, goal):
            goal_sound = mixer.Sound('goal.wav')
            goal_sound.play()
            finish = True
            win.reset()
        elif sprite.spritecollide(hero, enemies, False):
            explosion_sound = mixer.Sound('ex.wav')
            explosion_sound.play()
            finish = True
            loose.reset()
        elif sprite.spritecollide(hero, obstacles, False):
            explosion_sound = mixer.Sound('ex.wav')
            explosion_sound.play()
            finish = True
            loose.reset()
    sprite.groupcollide(bullets, walls, True, False) 
    sprite.groupcollide(bullets, enemies, True, True) 
    display.update()