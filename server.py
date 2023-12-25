import socket
from _thread import *
from player import Player
from ball import Ball
import pickle

server = "192.168.0.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(225,0,50,50,(255,0,0)), Player(225,450, 50,50, (0,0,255))]
ball = Ball(250, 250, 5, (0, 255, 0))

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            ball.move()
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            reply = [ball]

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply.append(players[0])
                else:
                    reply.append(players[1])

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
            
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1