import socket
from _thread import *
from player import Player
from ball import Ball
import pickle
from multiprocessing.connection import Listener

server = "localhost"
port = 5555

server_sock = Listener((server, port))

print("Waiting for a connection, Server Started")


players = [Player(225,0,50,50,(255,0,0)), Player(225,450, 50,50, (0,0,255))]
ball = Ball(250, 250, 15, 0, -0.5, (0, 255, 0))

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv())
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if currentPlayer == 2:
                    ball.move(players[player])
                    
                reply = [ball]
                if player == 1:
                    reply.append(players[0])
                else:
                    reply.append(players[1])

            conn.send(pickle.dumps(reply))
            
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn = server_sock.accept()

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1