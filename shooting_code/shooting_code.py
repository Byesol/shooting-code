# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 13
# Video link: https://www.youtube.com/watch?v=y2w-116htIQ
# Powerups (part 2)
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenney.nl
import pygame
import random
import numpy as np
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 600
HEIGHT = 800
FPS = 60

#level
level = 1

#attack 크기 및 속도
att_w = 70
att_h = 70
att_v = 5

boss_width = 200


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting code")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
#텍스트 및 텍슨트 사자
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    pygame.draw.rect(screen,BLACK,text_rect)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
def draw_exp_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 580
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
#이미지 그리기
def draw_pic(surf, x, y, img):
    img_rect = img.get_rect()
    img_rect.x = x 
    img_rect.y = y
    surf.blit(img, img_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (100, 80))        
        self.rect = self.image.get_rect()
        self.radius = 42
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        
       

    def update(self):
       
        #총알 속도 조정용 count,선택지별 lv mode_lv  플레이어 이동속도 spd
        global count,mode_lv,spd 
    

        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0
        count+=1
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -spd
        if keystate[pygame.K_RIGHT]:
            self.speedx = spd
        if keystate[pygame.K_DOWN]:
            self.speedy = spd
        if keystate[pygame.K_UP] :
            self.speedy = -spd
        if keystate[pygame.K_SPACE]and count%s_delay==0:
            self.shoot()
            
        if keystate[pygame.K_SPACE]and count%s2_delay==0:            
            
            if mode_lv[1]==0:
                _=1
            elif mode_lv[1]==1:
                self.shoot2()
                
            elif mode_lv[1]==1:
                self.shoot2()
                self.shoot2()
                
            else:
                self.shoot2()
                self.shoot2()
                self.shoot2()
                
            
     
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT:
            self.rect.right = HEIGHT
        if self.rect.bottom < 0:
            self.rect.left = 0



    def shoot2(self):  
        global mode_lv             
                     
        bullet3 = Bullet2(self.rect.centerx, self.rect.top)
 
        all_sprites.add(bullet3)
   
        bullets.add(bullet3)
        shoot_sound.play()    
        

    def shoot(self):    
        global mode_lv    
        if mode_lv[0]==0 or mode_lv[0]==1:  
            bullet = Bullet(self.rect.centerx, self.rect.top)                
            #bullet3 = Bullet2(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            #all_sprites.add(bullet3)
            bullets.add(bullet)
            #bullets.add(bullet3)
            shoot_sound.play()
        elif mode_lv[0]==2: 
            bullet2 = Bullet(self.rect.right-10, self.rect.top)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            bullet = Bullet(self.rect.left+10, self.rect.top)        
            
            all_sprites.add(bullet)            
            bullets.add(bullet)
            
            shoot_sound.play()
        else: 
            bullet = Bullet(self.rect.left-10, self.rect.top)                
            bullet2 = Bullet(self.rect.right+10, self.rect.top)
            all_sprites.add(bullet)
            all_sprites.add(bullet2)
            bullets.add(bullet)
            bullets.add(bullet2)
            shoot_sound.play()

         

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-80, -20)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -100 or self.rect.right > WIDTH + 100:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -3
        self.speedx = 0
    def update(self):    
        global mode_lv
        if mode_lv[0]==1:
            self.image = bullet3_img
        self.rect.y += self.speedy
        self.rect.x += self.speedx
       
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet2_img
        self.image.set_colorkey(BLACK)
        if mode_lv[1] > 0:
            self.image = bullet4_img
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -2
        self.speedx = random.randrange(-3,3)
    def update(self): 
        global mode_lv      
        self.rect.y += self.speedy
        self.rect.x += self.speedx
       
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Enemyattack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #required
        #self.image = pygame.Surface((att_w,att_h))
        self.image = pygame.transform.scale(boss_1, (att_w,att_h)  )
        
        self.rect = self.image.get_rect() #figures out rectangle based on image
        if boss1 != 0:
            self.rect.center = boss1.rect.center
        if boss2 != 0:
            self.rect.center = boss2.rect.center
        if boss3 != 0:
            self.rect.center = (random.randrange(0,600),random.randrange(0,100))
            
    
    def update(self):
        self.rect.y += att_v
        if stage ==2:
            self.rect.x += random.randrange(-5,5)  
            self.image = pygame.transform.scale(boss_2, (att_w,att_h)  )
        if stage ==3:
            
            self.image = pygame.transform.scale(boss_3, (att_w,att_h)  )      
        
        
     
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  
        global bosshp
        self.image = boss_1
        self.rect = self.image.get_rect()  
        self.rect.left = 200          
        self.rect.bottom = 200
        self.speedy = 0
        self.speedx = 2   
        if stage ==2: 
            self.speedy = 2
            self.speedx = 3   
        if stage ==3: 
            self.speedy = 4
            self.speedx = 5     
        self.boss_health = bosshp
    def update(self):          
        if stage ==2:
            self.image = boss_2
                     
        if stage ==3:
            self.image = boss_3
         
        if  self.rect.left < -100 or self.rect.right > WIDTH +100 :
            self.speedx *= -1
            
        if self.rect.bottom > HEIGHT or self.rect.top <0:            
            self.speedy *= -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.boss_health< 0:
            self.kill()
        

            

# Load all game graphics
background = pygame.image.load(path.join(img_dir, "back.jpeg"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "computer.png"))
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, "shot1.png")).convert()
bullet2_img = pygame.image.load(path.join(img_dir, "shot2.png"))
bullet3_img = pygame.image.load(path.join(img_dir, "shot3.png")).convert()
bullet4_img = pygame.image.load(path.join(img_dir, "shot4.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)



boss_1 = pygame.transform.scale(pygame.image.load(path.join(img_dir,'boss_1.png')), (boss_width, boss_width))
boss_2 = pygame.transform.scale(pygame.image.load(path.join(img_dir,'boss_2.jpg')), (boss_width, boss_width))
boss_3 = pygame.transform.scale(pygame.image.load(path.join(img_dir,'boss_3.png')), (boss_width, boss_width))
level_img = pygame.image.load(path.join(img_dir, "levelup.png"))
w1_img = pygame.image.load(path.join(img_dir, "w1.png"))
w2_img = pygame.image.load(path.join(img_dir, "w2.png"))
w3_img = pygame.image.load(path.join(img_dir, "w3.png"))



# Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'key.mp3'))
level_sound = pygame.mixer.Sound(path.join(snd_dir, 'level.mp3'))

expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'rumble1.ogg'))

pygame.mixer.music.load(path.join(snd_dir, 'cyber.wav'))
pygame.mixer.music.set_volume(0.3)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()

bullets = pygame.sprite.Group()

attacks = pygame.sprite.Group()
player = Player()

all_sprites.add(player)


for i in range(8):
    newmob()

#선책지 상자
choicelist = [pygame.Rect(60,280 ,150, 250), pygame.Rect(230,280 ,150, 250),pygame.Rect(400,280 ,150, 250)]

exp = 0

pygame.mixer.music.play(loops=-1)          
# Game loop
running = True

boss1 = 0
boss2 =0
boss3 =0
bosshp = 3
stage = 1
level = 1

mode_lv =  [0,0,0]
count =0

s_delay= 40
s2_delay= 60
max_exp = 100
spd=1
begin=1
end= 0
center=0


while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    if begin ==1:
        
        screen.blit(background, background_rect)
        
        draw_text(screen, "Press G to game start", 50, WIDTH / 2, 300)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    
                    begin=0
        pygame.display.flip()
    elif end == 1:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, background_rect)
        
        draw_text(screen, "You win!", 50, WIDTH / 2, 300)
        pygame.display.flip()
    elif end == 2:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, background_rect)
        
        draw_text(screen, "You Lose!", 50, WIDTH / 2, 300)
        pygame.display.flip()

    else:    
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        #경험치 초과, 레벨업
        if exp >max_exp:
            
            
            pygame.draw.rect(screen,(200,200,200),(30,200,550,400))
            draw_pic(screen,30,200,level_img)        
            
            for i in range(0,len(choicelist)): 
                pygame.draw.rect(screen,BLACK,choicelist[i])
            draw_pic(screen,60,280,w1_img)
            draw_pic(screen,230,280,w2_img)
            draw_pic(screen,400,280,w3_img)
            if event.type == pygame.MOUSEBUTTONDOWN:
                xPos, yPos = pygame.mouse.get_pos()
                for i in range(0,len(choicelist)): 
                    if choicelist[i].collidepoint(xPos, yPos):  
                        level_sound.play()
                        player.shield +=10            
                        mode_lv[i] +=1
                        if mode_lv[0]>2:
                            
                            s_delay /=2
                        if mode_lv[1]>2:
                            
                            s2_delay /=2               
                        print(i,mode_lv[i])     
                        spd = mode_lv[i]*2    
                        level +=1
                        exp = 0   
                        max_exp += 50                 
            
            pygame.display.flip()        
            
            
        else:
            
            # Update
            all_sprites.update()

            # check to see if a bullet hit a mob
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for hit in hits:
                
                exp += 50 - hit.radius
                random.choice(expl_sounds).play()
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            
                newmob()
            
            

            # check to see if a mob hit the player
            hits = pygame.sprite.spritecollide(player, mobs, True,pygame.sprite.collide_circle)
            for hit in hits:
                player.shield -= hit.radius * 2
                expl = Explosion(hit.rect.center, 'sm')
                all_sprites.add(expl)
                newmob()
                if player.shield <= 0:
                    player_die_sound.play()
                    death_explosion = Explosion(player.rect.center, 'player')
                    all_sprites.add(death_explosion)
                    player.hide()
                    player.lives -= 1
                    player.shield = 100

            #보스1
            if stage==1:
                if boss1 == 0:          
                    boss1 = Boss()     
                    all_sprites.add(boss1)                
                if boss1 !=0 and random.random()<0.01:                 
                    attack = Enemyattack()
                    all_sprites.add(attack)
                    attacks.add(attack)                                                      
                hits = pygame.sprite.spritecollide(player, attacks, True, pygame.sprite.collide_circle)
                for hit in hits:                   
                    player.shield -= 10 * 2 
                    expl = Explosion(hit.rect.center, 'sm')
                    all_sprites.add(expl)
                    if player.shield <= 0:
                        player_die_sound.play()
                        death_explosion = Explosion(player.rect.center, 'player')
                        all_sprites.add(death_explosion)
                        player.hide()
                        player.lives -= 1
                        player.shield = 100 
            
                
                hits = pygame.sprite.spritecollide(boss1, bullets, True, pygame.sprite.collide_circle)
                for hit in hits:
                    boss1.boss_health -=1
                    center = (hit.rect.centerx,hit.rect.top-10)
                    expl = Explosion(center, 'sm')
                    all_sprites.add(expl)
                    if boss1.boss_health <0:
                        all_sprites.remove(boss1)                    
                        stage=2
            elif stage==2:
                bosshp = 10
                if boss2 == 0:          
                    boss2 = Boss()     
                    all_sprites.add(boss2)                
                if boss2 !=0 and random.random()<0.04:                 
                    attack = Enemyattack()
                    all_sprites.add(attack)
                    attacks.add(attack)                                                      
                hits = pygame.sprite.spritecollide(player, attacks, True, pygame.sprite.collide_circle)
                for hit in hits:                   
                    player.shield -= 10 * 2 
                    expl = Explosion(hit.rect.center, 'sm')
                    all_sprites.add(expl)
                    if player.shield <= 0:
                        player_die_sound.play()
                        death_explosion = Explosion(player.rect.center, 'player')
                        all_sprites.add(death_explosion)
                        player.hide()
                        player.lives -= 1
                        player.shield = 100 
            
                
                hits = pygame.sprite.spritecollide(boss2, bullets, True, pygame.sprite.collide_circle)
                for hit in hits:
                    boss2.boss_health -=1
                    center = (hit.rect.centerx,hit.rect.top-10)
                    expl = Explosion(center, 'sm')
                    all_sprites.add(expl)
                    if boss2.boss_health <0:
                        all_sprites.remove(boss2)                    
                        stage=3
            #elif stage ==2
            elif stage==3:
                bosshp=30
                if boss3 == 0:          
                    boss3 = Boss()     
                    all_sprites.add(boss3)                
                if boss3 !=0 and random.random()<0.05:                 
                    attack = Enemyattack()
                    all_sprites.add(attack)
                    attacks.add(attack)                                                      
                hits = pygame.sprite.spritecollide(player, attacks, True, pygame.sprite.collide_circle)
                for hit in hits:                   
                    player.shield -= 10 * 2 
                    expl = Explosion(hit.rect.center, 'sm')
                    all_sprites.add(expl)
                    if player.shield <= 0:
                        player_die_sound.play()
                        death_explosion = Explosion(player.rect.center, 'player')
                        all_sprites.add(death_explosion)
                        player.hide()
                        player.lives -= 1
                        player.shield = 100 
            
                
                hits = pygame.sprite.spritecollide(boss3, bullets, True, pygame.sprite.collide_circle)
                for hit in hits:
                    boss3.boss_health -=1
                    center = (hit.rect.centerx,hit.rect.top-10)
                    expl = Explosion(center, 'sm')
                    all_sprites.add(expl)
                    if boss3.boss_health <0:
                        all_sprites.remove(boss3)                    
                        end=1
    
            
        

            # if the player died and the explosion has finished playing
            if player.lives == 0 and not death_explosion.alive():
                end =2

            # Draw / render
            
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
        
            draw_text(screen, "Level : "+str(level), 18, WIDTH / 2, 15)
            draw_text(screen, str(exp/max_exp*100)+"%", 18, WIDTH / 2, 35)
            draw_shield_bar(screen, 30, 30, player.shield)
            draw_exp_bar(screen, 5, 5, exp)
            draw_lives(screen, WIDTH - 100, 20, player.lives, player_mini_img)
            # *after* drawing everything, flip the display
        pygame.display.flip()

pygame.display.quit()
