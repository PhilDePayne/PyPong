import pygame
from network import Network
from player import Player
from ball import Ball
from button import Button

pygame.init()

def quit():
    print("Quit")
    pygame.quit()

def restart():
    connect()

def connect():
    global n
    global p
    print("Reconnect")
    n = Network()
    p = n.getP()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
screen = pygame.display.set_caption("Client")
quitButton = Button(win, quit, 200, 200, 140, 50)
replayButton = Button(win, restart, 200, 300, 140, 50)

n = None

def redrawWindow(win,player, player2, ball):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()

def main():
    run = True
    global n
    n = Network()
    global p
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        if n != None:
            ball, p2, result = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if result == 0:
            p.move()
            redrawWindow(win, p, p2, ball)
        else:
            quitButton.Update()
            replayButton.Update()
            n = None
            

main()  