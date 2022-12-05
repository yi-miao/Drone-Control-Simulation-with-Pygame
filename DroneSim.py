import pygame

pygame.init()

cap = "Drone Sim"
pygame.display.set_caption(cap)
(ww, wh) = (480, 480)       # display window size
screen = pygame.display.set_mode((ww, wh))

clock = pygame.time.Clock()

img00 = pygame.image.load("images/0.jpg").convert()
img0 = pygame.image.load("images/0.png").convert_alpha()
img0YL = pygame.image.load("images/0YL.png").convert_alpha()
img0YR = pygame.image.load("images/0YR.png").convert_alpha()
img1 = pygame.image.load("images/1.png").convert_alpha()
img12RL = pygame.image.load("images/12RL.png").convert_alpha()
img12RR = pygame.image.load("images/12RR.png").convert_alpha()
 
bg = img00
(bgw, bgh) = bg.get_size()
x0 = -(bgw-ww)/2    # Initial x
x1 = -(bgw-ww)      # maximum x value
y0 = -(bgh-wh)/2    # Initial y
y1 = -(bgh-wh)      # maximum y value
x = x0              # Initial x
y = y0              # Initial y

sf = img0
sfw, sfh = sf.get_size()

t = 0.05            # minimum change to the axis required
v = 5               # moving speed in ten gears
d = 0.2             # drift
r = 0               # angle when rolling 
s = 1               # scale 100%

joysticks = {}
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy

    cap = "Drone Sim"
    bg = img00
    sf = img0
    r = 0

    for joystick in joysticks.values():
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            # Left stick: X-axis turn (left or right)
            # Axis 0: Yaw or Rudder, left hand with Mode 2
            if i == 0:
                if axis < -t:
                    cap = "Yaw Left"            
                    sf = img0YL
                    if x < 0:
                        x -= v*axis
                    else:
                        x = x1
                if axis > t:
                    cap = "Yaw Right"
                    sf = img0YR
                    if x > x1:
                        x -= v*axis
                    else:
                        x = 0
            # Left stick: Y-axis go (up or down), altitude/height
            # Axis 1: Throttle, left hand with Mode 2
            if i == 1:
                if axis < -t:
                    cap = "Throttle Up" 
                    sf = img0                     
                    if y < 0:
                        y -= v*axis
                    else:
                        y = y1
                if axis > t:
                    cap = "Throttle Down"
                    sf = img0 
                    if y > y1:
                        y -= v*axis
                    else:
                        y = 0
            # Right stick: tilt (left or right)
            # Axis 2: Roll or Aileron, right hand with Mode 2
            if i == 2:
                if axis < -t:
                    cap = "Roll Left"           
                    sf = img12RL
                    if x < 0:
                        x -= v*axis*d
                        r = -25
                    else:
                        x = x1
                if axis > t:
                    cap = "Roll Right"
                    sf = img12RR
                    if x > x1:
                        x -= v*axis*d
                        r = 25
                    else:
                        x = 0
            # Right stick: tilt (forward or rear)
            # Axis 3: Pitch or Elevator, right hand with Mode 2
            if i == 3:
                if axis < -t:
                    cap = "Pitch Up"            
                    sf = img1
                    if y > y1:
                        y += v*axis*d
                    else:
                        y = 0
                if axis > t:
                    cap = "Pitch Down"
                    sf = img1
                    if y < 0:
                        y += v*axis*d
                    else:
                        y = y1
            if (i == 4) and (axis > t):
                v += v/10
            if (i == 5) and (axis > t):
                v = 5
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