import pygame 
import sys

class Button:  
    def __init__(self, screen):
        self.color_text = (255,255,255) 
        self.color_hovered = (170,170,170) 
        self.color = (100,100,100)
        self.smallfont = pygame.font.SysFont('Corbel',35)
        self.text = self.smallfont.render('quit' , True , self.color_text) 
        self.screen = screen

    def Update(self):
        while True: 

            for ev in pygame.event.get(): 

                if ev.type == pygame.QUIT: 
                    pygame.quit() 

                if ev.type == pygame.MOUSEBUTTONDOWN: 

                    #if the mouse is clicked on the 
                    # button the game is terminated 
                    if 500/2 <= mouse[0] <= 500/2+140 and 500/2 <= mouse[1] <= 500/2+40: 
                        pygame.quit() 

            # stores the (x,y) coordinates into 
            # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 

            # if mouse is hovered on a button it 
            # changes to lighter shade  
            if 500/2 <= mouse[0] <= 500/2+140 and 500/2 <= mouse[1] <= 500/2+40: 
                pygame.draw.rect(self.screen, self.color_hovered,[500/2,500/2,140,40]) 

            else: 
                pygame.draw.rect(self.screen, self.color, [500/2, 500/2, 140, 40]) 

            # superimposing the text onto our button 
            self.screen.blit(self.text , (500/2+50, 500/2)) 

            # updates the frames of the game 
            pygame.display.update() 