#LOST MEMORIES

#A GAME MADE FOR THE CODEFRIENDS FIRST GAMEJAM

#PLEASE READ THE README AND LISCENSE

#A HOW TO PLAY IS SPECICIFIED

"""
Imagine thinking I would comment the code lol.
"""

#THE CODE
import pygame, random

#set up stuff
pygame.init()

win = pygame.display.set_mode((1000, 600))

pygame.display.set_caption('Lost Memories')

gameIcon = pygame.image.load("./assets/images/icon.png")
pygame.display.set_icon(gameIcon)

clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()

sound = 1

pygame.mixer.music.load('./assets/music/main.mp3')
pygame.mixer.music.play(-1)

at = False
run = True
menu = 1
tia = False

#font
reg = pygame.font.Font("./assets/fonts/Virus_01.ttf", 30)

#images
bg = pygame.image.load('./assets/images/bg.png')
g0 = pygame.image.load('./assets/images/glitch0.png')
g1 = pygame.image.load('./assets/images/glitch1.png')
g2 = pygame.image.load('./assets/images/glitch2.png')
g3 = pygame.image.load('./assets/images/glitch3.png')
bgg0 = pygame.image.load('./assets/images/bgglitch0.png')
bgg1 = pygame.image.load('./assets/images/bgglitch1.png')
bf = pygame.image.load('./assets/images/blackfade.png')
rf = pygame.image.load('./assets/images/redfade.png')
ps = pygame.image.load('./assets/images/pause.png')
ta = pygame.image.load('./assets/images/terma.png')
end = pygame.image.load('./assets/images/end.png')
gl = [g0, g0, g0, g1, g2, g3, g0, g0, g0, g0, g0, g0, g0, g0, g0, g0, g0, g0]

#levels
l1 = pygame.image.load('./assets/levels/1.png')
l2 = pygame.image.load('./assets/levels/2.png')
l3 = pygame.image.load('./assets/levels/3.png')
l4 = pygame.image.load('./assets/levels/4.png')
l5 = pygame.image.load('./assets/levels/5.png')
l6 = pygame.image.load('./assets/levels/6.png')
l7 = pygame.image.load('./assets/levels/7.png')
l8 = pygame.image.load('./assets/levels/8.png')
l9 = pygame.image.load('./assets/levels/9.png')
l10 = pygame.image.load('./assets/levels/10.png')
circle = pygame.image.load('./assets/levels/circle.png')
up = pygame.image.load('./assets/levels/up.png')
down = pygame.image.load('./assets/levels/down.png')
left = pygame.image.load('./assets/levels/left.png')
right = pygame.image.load('./assets/levels/right.png')
none = pygame.image.load('./assets/levels/none.png')
locki = pygame.image.load('./assets/levels/keyhole.png')
key = pygame.image.load('./assets/sprite/key.png')

#sprite
p = pygame.image.load('./assets/sprite/player.png')
p1 = pygame.image.load('./assets/sprite/player1.png')
p2 = pygame.image.load('./assets/sprite/player2.png')
d1 = pygame.image.load('./assets/sprite/dead1.png')
d2 = pygame.image.load('./assets/sprite/dead2.png')
d3 = pygame.image.load('./assets/sprite/dead3.png')
d4 = pygame.image.load('./assets/sprite/dead4.png')

#sound effects
select = pygame.mixer.Sound("./assets/music/clap.wav")

#functions
def mutesound():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if sound == 1:
                        mutesound()
                        sound = 0
                    elif sound == 0:
                        sound = 1
                        unpause()
                if menu == 1:
                    if event.key == pygame.K_r:
                        select.play()
                        win.fill((0,0,0))
                        menu = 2
                        pygame.mixer.music.load('./assets/music/storyline.wav')
                        pygame.mixer.music.play(0)
                        t = 0
                    if event.key == pygame.K_1:
                        direction = 'none'
                        pygame.mixer.music.stop()
                        cxpos = 0
                        cypos = 0
                        menu = 3
                        level = 10
                        lock = True
                        select.play()
                        win.fill((0,0,0))
                        px = 100
                        py = 100
                        cc = 0
                        offset=0
                        yoffset = 0
                        pygame.mixer.music.load('./assets/music/music.mp3')
                        pygame.mixer.music.play(-1)
                if menu == 3:
                    if event.key == pygame.K_p:
                        bfc = 0
                        menu = 6
                    if event.key == pygame.K_n:
                        bfc = 0
                        menu = 4
                    if event.key == pygame.K_b:
                        bfc = 0
                        menu = 9
                    if event.key == pygame.K_l:
                        print(f"{px+offset}, {py+yoffset}")
                    if event.key == pygame.K_r:
                        if tia == True:
                            tia = False
                        elif at == True:
                            tia = True
                            text = open(f'./assets/levels/{level}.txt').read()
                            ttext = reg.render(text, True, (255, 255, 255))
                            ttextr = ttext.get_rect()
                            ttextr.center = (500,200)
                            trtext = reg.render('PRESS R TO EXIT TERMINAL', True, (255, 255, 255))
                            trtextr = trtext.get_rect()
                            trtextr.center = (500, 300)
                        else:
                            pass
                            
                if menu == 7:
                    if event.key == pygame.K_p:
                        pygame.mixer.music.load('./assets/music/music.mp3')
                        pygame.mixer.music.play(-1)
                        menu = 3
                    if event.key == pygame.K_ESCAPE:
                        menu = 1
                        pygame.mixer.music.load('./assets/music/main.mp3')
                        pygame.mixer.music.play(-1)
                if menu == 1 or menu == 2:
                    if event.key == pygame.K_n:
                        pygame.mixer.music.stop()
                        menu = 3
                        level = 1
                        select.play()
                        win.fill((0,0,0))
                        px = 100
                        py = 100
                        offset=0
                        yoffset = 0
                        pygame.mixer.music.load('./assets/music/music.mp3')
                        pygame.mixer.music.play(-1)
                        
    if menu == 1:
        win.blit(bg, (0,0))
    if menu == 2:
        win.blit(random.choice(gl), (0,0))
        t += 1
        if t == 2880:
            level = 1
            px = 100
            py = 100
            offset=0
            yoffset = 0
            pygame.mixer.music.load('./assets/music/music.mp3')
            pygame.mixer.music.play(-1)
            menu = 3
    if menu == 3:
       keys = pygame.key.get_pressed()
       blocked = False
       screensurf = pygame.display.get_surface()
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           direction = 'right'
           for num in range(py, py+21):
                bcol = screensurf.get_at((px+21, num))[:3]
                if bcol == (0,0,0):
                    blocked = True
           if blocked != True:
               if px < 600:
                   px+=1
               else:
                   offset = offset+1
       if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           direction = 'left'
           for num in range(py, py+21):
                bcol = screensurf.get_at((px-1, num))[:3]
                if bcol == (0,0,0):
                    blocked = True
           if blocked != True:
               if offset != 0 and px < 400:
                   offset -= 1
               else:
                   px-=1
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           direction = 'down'
           for num in range(px-1, px+21):
                bcol = screensurf.get_at((num, py+21))[:3]
                if bcol == (0,0,0):
                    blocked = True
           if blocked != True:
               if py < 400:
                   py+=1
               else:
                    yoffset+=1
       if keys[pygame.K_UP] or keys[pygame.K_w]:
           direction = 'up'
           for num in range(px-1, px+21):
                bcol = screensurf.get_at((num, py-1))[:3]
                if bcol == (0,0,0):
                    blocked = True
           if blocked != True:
               if yoffset > 0 and py < 300:
                   yoffset-=1
                   print(yoffset)
               else:
                   py-=1
       for num in range(px-1, px+21):
           for num2 in range(py-1, py+21):
               bcol = screensurf.get_at((num, num2))[:3]
               if bcol == (255,202,24):
                   bfc = 0
                   menu = 4
               if bcol == (236, 28, 36) or bcol == (255, 244, 0):
                   bfc = 0
                   menu = 5
               if bcol == (255, 255, 255):
                   at = True
               else:
                   at = False
               if bcol == (255, 242, 0):
                   lock = False
       if level == 9:
           if cc < 2880:
               cc += 1
               print(cc)
               ml = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.5,-0.5,-1,-1,1,1,1,1,1,2]
               iml = [0,0,0,0,0,0,0,-1,-1,-1,-1,-2,-2,-2]
               if cypos > 8640:
                   cypos += random.choice(iml)
               elif cypos > 500:
                   fr = random.randint(1,2)
                   if fr == 2:
                       cypos += random.choice(iml)
                   if fr == 1:
                       cypos += random.choice(ml)
               else:
                   cypos += random.choice(ml)
               cxpos += random.choice(ml)
           else:
               bfc = 0
               menu = 4
       if level == 8:
           screensurf = pygame.display.get_surface()
           if direction == 'none':
               win.blit(none, (0,0))
           if direction == 'up':
               win.blit(up, (0,0))
           if direction == 'down':
               win.blit(down, (0,0))
           if direction == 'right':
               win.blit(right, (0,0))
           if direction == 'left':
               win.blit(left, (0,0))
       if level == 1:
           fr = random.randint(1,2)
           if fr == 1:
               win.blit(l1, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
               win.blit(l1, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 2:
           fr = random.randint(1,2)
           if fr == 1:
               win.blit(l2, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
               win.blit(l2, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 3:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l3, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l3, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 4:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l4, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                if lock == True:
                   win.blit(locki, (1569-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]), 344-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                   win.blit(key, (51-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]), 1069-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l4, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                if lock == True:
                   win.blit(locki, (1569-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]), 344-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                   win.blit(key, (51-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]), 1069-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 5:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l5, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l5, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 6:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l6, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                if lock == True:
                   win.blit(locki, (851-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]), 286-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                   win.blit(key, (280-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]), 247-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l6, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                if lock == True:
                   win.blit(locki, (851-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]), 286-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
                   win.blit(key, (280-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]), 247-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 7:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l7, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l7, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 8:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l8, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l8, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 9:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l9, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l9, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           win.blit(circle, (cxpos-offset, cypos-yoffset))
       if level == 10:
           fr = random.randint(1,2)
           if fr == 1:
                win.blit(l10, (0-offset-random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset+random.choice([0,0,0,0,0,0,0,0,0,1,2])))
           else:
                win.blit(l10, (0-offset+random.choice([0,0,0,0,0,0,0,0,0,1,2]),0-yoffset-random.choice([0,0,0,0,0,0,0,0,0,1,2])))
       if level == 8:
           screensurf = pygame.display.get_surface()
           if direction == 'up':
               for num in range(px-1, px+21):
                    bcol = screensurf.get_at((num, py-1))[:3]
                    if bcol == (0,0,0):
                        blocked = True
               if blocked != True:
                   if yoffset > 0 and py < 300:
                       yoffset-=4
                       print(yoffset)
                   else:
                       py-=4
           if direction == 'down':
               for num in range(px-1, px+21):
                    bcol = screensurf.get_at((num, py+21))[:3]
                    if bcol == (0,0,0):
                        blocked = True
               if blocked != True:
                   if py < 400:
                       py+=4
                   else:
                       yoffset+=4
           if direction == 'left':
               for num in range(py, py+21):
                   bcol = screensurf.get_at((px-1, num))[:3]
                   if bcol == (0,0,0):
                       blocked = True
               print(blocked)
               if blocked != True:
                   if offset != 0 and px < 400:
                       offset -= 4
                   else:
                       px-=4
           if direction == 'right':
               for num in range(py, py+21):
                    bcol = screensurf.get_at((px+21, num))[:3]
                    if bcol == (0,0,0):
                        blocked = True
               if blocked != True:
                   if px < 600:
                       px+=4
                   else:
                       offset = offset+4

       if level == 11:
           pygame.mixer.music.stop()
           pygame.mixer.music.load('./assets/music/victoryc.mp3')
           pygame.mixer.music.play(0)
           menu = 8

               
    
       fr = random.randint(1,10)
       if fr == 10:
           win.blit(bgg0, (0,0))
       if fr == 9:
           win.blit(bgg1, (0,0))
       fr = random.randint(1,10)
       if fr == 10:
           win.blit(p1, (px, py))
       elif fr == 9:
           win.blit(p2, (px, py))
       else:
           win.blit(p, (px, py))
       if at == True:
           if tia != True:
              win.blit(ta, (-150,0))
       if tia == True:
           win.blit(ttext, ttextr)
           win.blit(trtext, trtextr)
    if menu == 4:
        bfc+=1
        print(bfc)
        if bfc == 100:
            direction = 'none'
            cc = 0
            cxpos = 0
            cypos = 0
            level+=1
            if level == 4 or level == 6:
                lock = True
            px = 100
            py = 100
            offset = 0
            yoffset = 0
            menu = 3
        else:
            win.blit(bf, (0,0))
    if menu == 5:
        bfc+=1
        if bfc == 0:
            win.blit(d1, (px-10, py-10))
        if bfc == 5:
            win.blit(d2, (px-10, py-10))
        if bfc == 10:
            win.blit(d3, (px-10, py-10))
        if bfc == 15:
            win.blit(d4, (px-10, py-10))
        if bfc == 100:
            px = 100
            py = 100
            offset = 0
            yoffset = 0
            cc = 0
            cxpos = 0
            cypos = 0
            direction = 'none'
            if level == 4 or level == 6:
                lock = True
            menu = 3
        elif bfc > 90 and bfc < 100:
            pass
        else:
            win.blit(rf, (0,0))
    if menu == 6:
        bfc+=1
        print(bfc)
        if bfc == 50:
            win.blit(ps, (0,0))
            pygame.mixer.music.load('./assets/music/pause.mp3')
            pygame.mixer.music.play(0)
            menu = 7
        else:
            win.blit(bf, (0,0))
    if menu == 8:
        win.blit(end, (0,0))
    if menu == 9:
        bfc+=1
        print(bfc)
        if bfc == 100:
            direction = 'none'
            cc = 0
            cxpos = 0
            cypos = 0
            level-=1
            if level == 0:
                level = 1
            if level == 4 or level == 6:
                lock = True
            px = 100
            py = 100
            offset = 0
            yoffset = 0
            menu = 3
        else:
            win.blit(bf, (0,0))
        

    clock.tick(144) #144 fps
    pygame.display.update()
pygame.quit()
