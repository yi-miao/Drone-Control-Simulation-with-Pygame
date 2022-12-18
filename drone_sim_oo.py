import pygame
import random
import numpy as np

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
CURSOR = (20, 8)
WINDOW = (480, 480)
PARAM_DO = 0.01
PARAM_DK = 1.2
PARAM_AG = 45
PARAM_SP = 10
        
class Game:
    def __init__(self):
        pygame.init()
        (self.ww, self.wh) = WINDOW
        self.center=(self.ww//2, self.wh//2)     
        self.screen = pygame.display.set_mode(WINDOW)
        self.surface0 = pygame.Surface(CURSOR, pygame.SRCALPHA)
        self.surface0.fill(WHITE)
        (self.sw0, self.sh0) = CURSOR
        (self.sw, self.sh) = (self.sw0, self.sh0)
        self.angle = 0
        self.points=[]
        for i in range(1000):
            n1 = random.randrange(-5000,5000)
            n2 = random.randrange(-5000,5000)
            n3 = random.randrange(-5000,5000)
            self.points.append([n1,n2,n3])

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.move(event.key)
                elif event.type == pygame.QUIT:
                    running = False
                    break                    
            self.update() 
            
        pygame.quit()

    def move(self, key):   
        self.angle = 0
        (self.sw, self.sh) = (self.sw0, self.sh0)
        if key == pygame.K_LEFT:
            self.angle = PARAM_AG
            for p in self.points:
                p[0], p[2] = np.cos(-PARAM_DO)*p[0]-np.sin(-PARAM_DO)*p[2], np.sin(-PARAM_DO)*p[0]+np.cos(-PARAM_DO)*p[2]               
        if key == pygame.K_RIGHT:
            self.angle = -PARAM_AG
            for p in self.points:
                p[0], p[2] = np.cos(PARAM_DO)*p[0]-np.sin(PARAM_DO)*p[2], np.sin(PARAM_DO)*p[0]+np.cos(PARAM_DO)*p[2] 
        if key == pygame.K_UP:
            (self.sw, self.sh) = (int(self.sw0*PARAM_DK), int(self.sh0*PARAM_DK))  
            for p in self.points:
                p[2] += PARAM_SP  
        if key == pygame.K_DOWN:
            (self.sw, self.sh) = (self.sw0//PARAM_DK, self.sh0//PARAM_DK)   
            for p in self.points:
                p[2] -= PARAM_SP    
                
    def update(self):          
        for p in self.points:
            if p[2]<=-5000 or p[2]>=5000:
                p[0], p[1], p[2] = random.randrange(-5000,5000), random.randrange(-5000,5000), 5000
            else:
                if p[2]<=0:
                    pass
                else:
                    try:
                        w = p[2] * 30 / 5000
                        pygame.draw.circle(self.screen,WHITE,(int(p[0]/w+self.center[0]),int(p[1]/w+self.center[1])),int(10/w))
                    except:
                        print("failed to draw circle.")

        surface = pygame.transform.scale(self.surface0, (self.sw, self.sh)) 
        rotated_surface = pygame.transform.rotate(surface, self.angle)
        rect = rotated_surface.get_rect(center = (self.ww//2, self.wh//2))
        self.screen.blit(rotated_surface, (rect.x, rect.y))
        
        pygame.display.update()

game = Game()
game.run()   
