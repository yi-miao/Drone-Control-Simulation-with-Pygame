import pygame

pygame.init()

cap = "Drone Sim"
screen = pygame.display.set_mode((360, 360))
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
sf = img0

done = False
black = (0,0,0)
x0 = -1100
y0 = -620
x = x0
y = y0
v = 10
t = 0.08
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
    
    for joystick in joysticks.values():
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            if (i == 0) and (axis < -t):
                sf = img0YL
                if x < 0:
                    x -= v*axis
                    cap = "Yaw Left"
            if (i == 0) and (axis > t):
                sf = img0YR
                if x > -2200:
                    x -= v*axis
                    cap = "Yaw Right"
            if (i == 1) and (axis < -t):
                sf = img0
                y += v*axis*0.2
                cap = "Throttle Up"
            if (i == 1) and (axis > t):
                sf = img0
                y += v*axis*0.2
                cap = "Throttle Down"
            if (i == 2) and (axis < -t):
                sf = img12RL
                x += v*axis*0.2
                cap = "Roll Left"
            if (i == 2) and (axis > t):
                sf = img12RR
                x += v*axis*0.2
                cap = "Roll Right"
            if (i == 3) and (axis < -t):
                sf = img1
                if y > -1230:
                    y += v*axis
                    cap = "Pitch Up"
            if (i == 3) and (axis > t):
                sf = img1
                if y < -10:
                    y += v*axis
                    cap = "Pitch Down"
            if (i == 4) and (axis > t):
                v += v/10
            if (i == 5) and (axis > t):
                v = 10
                x = x0
                y = y0

    pygame.display.set_caption(cap + ': ' + str(round(x,0)) + ' , ' + str(round(y,0)))  
    screen.blit(bg, (x, y))
    screen.blit(sf, (107, 107))
    pygame.display.update()

    clock.tick(30)

pygame.quit()