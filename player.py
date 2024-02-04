import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.direction = "STALE" #LEFT, STALE, RIGHT #TODO: enum

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def getLeft(self):
        return self.x
    
    def getRight(self):
        return self.x + self.width
    
    def getTop(self):
        return self.y
    
    def getBottom(self):
        return self.y + self.height
    
    def getCenter(self):
        return (self.x + self.width/2, self.y + self.height/2)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.direction = "LEFT"
                self.x -= self.vel

        elif keys[pygame.K_RIGHT]:
            if self.x < 450:
                self.direction = "RIGHT"
                self.x += self.vel
                
        else:
            self.direction = "STALE"

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)