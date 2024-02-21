import pygame 
import sys

class Button:  
    def __init__(self, screen, onClickFunc, x, y , w, h, label):
        self.color_text = (255,255,255) 
        self.color_hovered = (170,170,170) 
        self.color = (100,100,100)
        self.smallfont = pygame.font.SysFont('Corbel',35)
        self.text = self.smallfont.render(label , True , self.color_text) 
        self.screen = screen
        self.OnClick = onClickFunc
        self.x = x 
        self.y = y
        self.w = w
        self.h = h

    def Update(self, event):

        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 

        for ev in event: 

            if ev.type == pygame.QUIT: 
                pygame.quit() 

            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                print("Clicked")
                if self.x <= mouse[0] <= self.x+self.w and self.y <= mouse[1] <= self.y+self.h: 
                    self.OnClick()

        # if mouse is hovered on a button it 
        # changes to lighter shade  
        if self.x <= mouse[0] <= self.x+self.w and self.y <= mouse[1] <= self.y+self.h: 
            pygame.draw.rect(self.screen, self.color_hovered,[self.x,self.y,self.w,self.h]) 

        else: 
            pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h]) 

        # superimposing the text onto our button 
        self.screen.blit(self.text , (self.x+50, self.y)) 

        # updates the frames of the game 
        pygame.display.update() 