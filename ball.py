import pygame
import numpy as np
import random

class Ball:
    def __init__(self, x, y, r, vX, vY, color):
        self.x = x
        self.y = y
        self.r = r
        self.vX = vX
        self.vY = vY
        self.color = color
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
        
    def detect_collision(self, player):
        tmpX = self.x
        tmpY = self.y
        
        if self.x < player.x:
            tmpX = player.x
        elif self.x > player.x + player.width:
            tmpX = player.x + player.width
            
        if self.y < player.y:
            tmpY = player.y
        elif self.y > player.y + player.height:
            tmpY = player.y + player.height
            
        distX = self.x - tmpX
        distY = self.y - tmpY
        distance = distX*distX + distY*distY
        
        return self.r*self.r > distance
    
    def resolve_collision(self, player):
        if self.detect_collision(player):
            
            separation = [0,0]
            closest = (np.clip(self.x, player.getLeft(), player.getRight()), 
                       np.clip(self.y, player.getTop(), player.getBottom()),
                       0)
            
            if self.x == closest[0] and self.y == closest[1]:
            
                left = self.x - player.getLeft() + self.r
                right = player.getRight() - self.x + self.r
                
                top = self.y - player.getTop() + self.r
                bottom = player.getBottom() - self.y + self.r
                
                if left < right:
                    separation[0] = -left
                else: 
                    separation[0] = right
                    
                if top < bottom:
                    separation[1] = -top
                else:
                    separation[1] = bottom
                    
                print(separation)
                    
                if abs(separation[0]) < abs(separation[1]):
                    separation[1] = 0
                    if player.direction == "LEFT":
                        self.vX = -random.random() + 3.2
                    elif player.direction == "RIGHT":
                        self.vX = random.random() + 3.2

                if abs(separation[0]) > abs(separation[1]):
                    separation[0] = 0
                    if player.direction == "LEFT":
                        self.vX = random.random() + 3.2
                    elif player.direction == "RIGHT":
                        self.vX = -random.random() + 3.2
                    
                self.x += separation[0]
                self.y += separation[1]
                
                self.vY = -self.vY
                
                return True
            
            else:
                denom = np.linalg.norm(np.array((self.x, self.y, 0)) - np.array(closest)) * (self.r - np.linalg.norm(np.array((self.x, self.y, 0)) - np.array(closest)))
                center = player.getCenter()
                separation[0] = (self.x - center[0]) / denom
                separation[1] = (self.y - center[1]) / denom
                self.x += separation[0]/4
                self.y += separation[1]/4
                
                self.vY = -self.vY #TODO: change if y > player.y

                if self.y < player.getBottom():
                    print(1)
                    print(player.direction)
                    if player.direction == "LEFT":
                        self.vX = -random.random() - 3.2
                    elif player.direction == "RIGHT":
                        self.vX = random.random() + 3.2
                else:
                    if player.direction == "LEFT":
                        self.vX = random.random() + 3.2
                    elif player.direction == "RIGHT":
                        self.vX = -random.random() - 3.2
                    
                return True
				   
        return False
                
    def move(self, player):
        
        if not self.resolve_collision(player):
            if self.x <= (0 + self.r) or self.x >= (500 - self.r): #TODO: magic numbers, window size in const file
                self.vX = -self.vX

        self.x += self.vX
        self.y += self.vY

        if self.y < (0 - self.r): #TODO: magic numbers, window size in const file
            return 1
        elif self.y > (500 + self.r): #TODO: magic numbers, window size in const file    
            return 2
        else:
            return 0
                