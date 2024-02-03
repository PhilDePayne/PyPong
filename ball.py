import pygame

class Ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
        
    def detect_collision(self, player):
        tmpX = self.x
        tmpY = self.y
        
        if self.x < player.x:
            tmpX = player.x
        elif self.x > player.x + player.w:
            tmpX = player.x + player.w
            
        if self.y < player.y:
            tmpY = player.y
        elif self.y > player.y + player.h:
            tmpY = player.y + player.h
            
        distX = self.x - tmpX
        distY = self.y - tmpY
        distance = distX*distX + distY*distY
        
        return self.r*self.r >= distance
    
    def resolve_collision(self, player):
        if self.detect_collision(player):
            left = self.x - (player.x - player.w/2) + self.r
            right = (player.x + player.w/2) - self.x + self.r
            
            top = self.y - (player.y - player.h/2) + self.r
            bottom = (player.y - player.h/2) - self.y + self.r
            
            separation = [0,0]
            
            if left < right:
                separation[0] = -left
            else: 
                separation[0] = right
                
            if top < bottom:
                separation[1] = -top
            else:
                separation[1] = bottom
                
            if abs(separation[0]) < abs(separation[1]):
                separation[1] = 0
            if abs(separation[0]) > abs(separation[1]):
                separation[0] = 0
                
            self.x += separation[0]
            self.y += separation[1]
            
                
    def move(self, player):
        self.y += 2
        self.resolve_collision(player)
