import pygame

pygame.init()

screen = pygame.display.set_mode((360, 360))
cap = "Drone Sim"
pygame.display.set_caption(cap)

clock = pygame.time.Clock()

joysticks = {}

img0 = pygame.image.load("images/0.jpg").convert()

done = False
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

    screen.fill((0, 0, 0))
    cap = "Drone Sim"
    img = img0
    
    for joystick in joysticks.values():
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            if (i == 0) and (axis < -t):
#                img = img0YL
                if x > -2190:
                    x += v*axis
                    cap = "Yaw Left"
            if (i == 0) and (axis > t):
#                img = img0YR
                if x < -10:
                    x += v*axis
                    cap = "Yaw Right"
            if (i == 1) and (axis < -t):
#                img = img0
                    y += v*axis
                    cap = "Throttle Up"
            if (i == 1) and (axis > t):
#                img = img0
                    y += v*axis
                    cap = "Throttle Down"
            if (i == 2) and (axis < -t):
#                img = img12RL
                x += v*axis*0.2
                cap = "Roll Left"
            if (i == 2) and (axis > t):
#                img = img12RR
                x += v*axis*0.2
                cap = "Roll Right"
            if (i == 3) and (axis < -t):
#                img = img1
                if y > -1230:
                    y += v*axis
                    cap = "Pitch Up"
            if (i == 3) and (axis > t):
#                img = img1
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
    screen.blit(img, (x, y))
    pygame.display.update()

    clock.tick(30)

pygame.quit()