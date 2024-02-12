import socket
import pickle
from multiprocessing.connection import Client


class Network:
    def __init__(self):
        self.server = "localhost"
        self.port = 5555
        self.client = Client((self.server, self.port))
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            return pickle.loads(self.client.recv())
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv())
        except socket.error as e:
            print(e)