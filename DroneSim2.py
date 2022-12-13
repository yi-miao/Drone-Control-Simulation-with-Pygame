import pygame
import random
import numpy as np

pygame.init()

(ww, wh) = (480,480)
center=(int(ww/2),int(wh/2))
screen = pygame.display.set_mode((ww, wh))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

(sw0, sh0) = (20, 8)
surface0 = pygame.Surface((sw0, sh0), pygame.SRCALPHA)
surface0.fill(WHITE)
(sw, sh) = (sw0, sh0)

#Stars [x, y, z]
points=[]
for i in range(1000):
    n1 = random.randrange(-5000,5000)
    n2 = random.randrange(-5000,5000)
    n3 = random.randrange(-5000,5000)
    points.append([n1,n2,n3])

do=0.01
angle = 0
dr=45

ds=10
dk=1.2

joystick = None
clock  = pygame.time.Clock()
run=True
while run:
    screen.fill(BLACK)
    angle = 0
    (sw, sh) = (sw0, sh0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if joystick:
        axis_x, axis_y = (joystick.get_axis(0), joystick.get_axis(1))
        if abs(axis_x) > 0.1:  
            if axis_x > 0:
                for p in points:
                    p[0], p[2] = np.cos(do)*p[0]-np.sin(do)*p[2], np.sin(do)*p[0]+np.cos(do)*p[2] 
            else:
                for p in points:
                    p[0], p[2] = np.cos(-do)*p[0]-np.sin(-do)*p[2], np.sin(-do)*p[0]+np.cos(-do)*p[2]            
            angle = -dr*axis_x  
        if abs(axis_y) > 0.1:
            if axis_y > 0:
                for p in points:
                    p[2] += ds  
                (sw, sh) = (int(sw0*dk), int(sh0*dk))                     
            else:   
                for p in points:
                    p[2] -= ds       
                (sw, sh) = (int(sw0/dk), int(sh0/dk))                    
    else:
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            
    for p in points:
        #this is to create new stars
        if p[2]<=-5000 or p[2]>=5000:
            p[0], p[1], p[2] = random.randrange(-5000,5000), random.randrange(-5000,5000), 5000
        else:
            #this is to ignore stars which are behind the ship
            if p[2]<=0:
                pass
            else:
                try:
                    w = p[2] * 30 / 5000
                    pygame.draw.circle(screen,(255,255,255),(int(p[0]/w+center[0]),int(p[1]/w+center[1])),int(10/w))
                except:
                    print("failed to draw circle.")

    surface = pygame.transform.scale(surface0, (sw, sh)) 
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (int(ww/2), int(wh/2)))
    screen.blit(rotated_surface, (rect.x, rect.y))
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()