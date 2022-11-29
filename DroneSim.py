import pygame

pygame.init()

cap = "Drone Sim"
(ww, wh) = (480, 480)
screen = pygame.display.set_mode((ww, wh))
pygame.display.set_caption(cap)

clock = pygame.time.Clock()

joysticks = {}

img00 = pygame.image.load("images/0.jpg").convert()
img0 = pygame.image.load("images/0.png").convert_alpha()
img0YL = pygame.image.load("images/0YL.png").convert_alpha()
img0YR = pygame.image.load("images/0YR.png").convert_alpha()
img1 = pygame.image.load("images/1.png").convert_alpha()
img12RL = pygame.image.load("images/12RL.png").convert_alpha()
img12RR = pygame.image.load("images/12RR.png").convert_alpha()
 
bg = img00
bgw, bgh = bg.get_size()
sf = img0
sfw, sfh = sf.get_size()

done = False
black = (0,0,0)
x0 = -(bgw-ww)/2
x1 = -(bgw-ww)
y0 = -(bgh-wh)/2
y1 = -(bgh-wh)
x = x0
y = y0
v = 10
t = 0.05
r = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True  
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                joystick = joysticks[event.instance_id]
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]

    screen.fill(black)
    cap = "Drone Sim"
    bg = img00
    sf = img0
    r = 0
    
    for joystick in joysticks.values():
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            if (i == 0) and (axis < -t):
                cap = "Yaw Left"
                sf = img0YL
                if x < 0:
                    x -= v*axis
            if (i == 0) and (axis > t):
                cap = "Yaw Right"
                sf = img0YR
                if x > x1:
                    x -= v*axis
            if (i == 1) and (axis < -t):
                cap = "Throttle Up"
                sf = img0 
                if y > y1:
                    y += v*axis*0.2
            if (i == 1) and (axis > t):
                cap = "Throttle Down"
                sf = img0
                if y < 0:
                    y += v*axis*0.2
            if (i == 2) and (axis < -t):
                cap = "Roll Left"
                sf = img12RL
                if x < 0:
                    x -= v*axis*0.2
                    r = 25
            if (i == 2) and (axis > t):
                cap = "Roll Right"
                sf = img12RR
                if x > x1:
                    x -= v*axis*0.2
                    r = -25
            if (i == 3) and (axis < -t):
                cap = "Pitch Up"
                sf = img1
                if y > y1:
                    y += v*axis
            if (i == 3) and (axis > t):
                cap = "Pitch Down"
                sf = img1
                if y < 0:
                    y += v*axis
            if (i == 4) and (axis > t):
                v += v/10
            if (i == 5) and (axis > t):
                v = 10
                x = x0
                y = y0
                
    pygame.display.set_caption(cap + ': ' + str(round(x,0)) + ' , ' + str(round(y,0)))  
    if r != 0:
        rotated_bg = pygame.transform.rotate(bg, r)
        new_rect = rotated_bg.get_rect(center = bg.get_rect(topleft = (x, y)).center)
        screen.blit(rotated_bg, new_rect)
    else:
        screen.blit(bg, (x, y))
    screen.blit(sf, (180, 180))
    pygame.display.update()

    clock.tick(30)

pygame.quit()