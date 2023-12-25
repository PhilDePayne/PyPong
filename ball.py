import pygame

class Ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
        
    def detect_collision(self, rect):
        tmpX = self.x
        tmpY = self.y
        
        if self.x < rect.x:
            tmpX = rect.x
        elif self.x > rect.x + rect.w:
            tmpX = rect.x + rect.w
            
        if self.y < rect.y:
            tmpY = rect.y
        elif self.y > rect.y + rect.h:
            tmpY = rect.y + rect.h
            
        distX = self.x - tmpX
        distY = self.y - tmpY
        distance = distX*distX + distY*distY
        
        return self.r*self.r >= distance
    
    #def resolve_collision(self, rect):
        #if self.detect_collision(rect):
        
    def move(self):
        self.y += 2
            
