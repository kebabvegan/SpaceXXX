import sys
import socket
import json
import time
import threading

TAILLE_TAMPON = 256

class Client:

    def __init__(self):
        self.sock_server = socket.socket()
        # print('Connexion vers localhost: ' + str(sys.argv[1]) + 'reussie')

    def connclient(self, ipserver, portserver):
        self.sock_server.connect((ipserver, portserver))

    def sendmsg(self, msg):
        data = json.dumps(msg)
        if data == 0:
            raise RuntimeError("LOL")
        self.sock_server.send(data.encode())

    # def reply(self):
    #     while True:
    #         wrapper = self.sock_server.makefile()
    #         txt = wrapper.readline()
    #         print(txt)
    #         time.sleep(1)

    def reply(self):
        response = self.sock_server.recv(TAILLE_TAMPON).decode()
        response = json.loads(response)
        return response

    def login_request(self, pseudo):
        request = {
            "pseudo": pseudo,
            "exchange": "login"
        }
        self.sendmsg(request)
        return self.reply()

    def logout_request(self, pseudo):
        request = {
            "pseudo": pseudo,
            "exchange": "logout"
        }
        self.sendmsg(request)
        self.sock_server.close()
        return self.reply()

    def placement_request(self, coord):
        request = {
            "exchange": "placement",
            "data": {
                [coord[1], coord[2]]
            }
        }
        self.sendmsg(request)
        return self.reply()

    def move_request(self, nb):
        request = {
            "exchange": "move",
            "data": {nb}
        }
        self.sendmsg(request)
        return self.reply()

    def pause_request(self):
        request = {
            "exchange": "pause"
        }
        self.sendmsg(request)
        return self.reply()

    def continue_request(self):
        request = {
            "exchange": "continue"
        }
        self.sendmsg(request)
        return self.reply()

    def listof_request(self):
        request = {
            "exchange": "listof"
        }
        self.sendmsg(request)
        return self.reply()

    def mod_request(self, newpseudo):
        request = {
            "exchange": "mod",
            "data": newpseudo
        }
        self.sendmsg(request)
        return self.reply()

    def refresh_request(self):
        request = {
            "exchange": "refresh"
        }
        self.sendmsg(request)
        return  self.reply()

    def getstrat_request(self, pseudo_source, pseudo_dest, port_num):
        request = {
            "pseudo": pseudo_source,
            "exchange": "getstrat",
            "data": {
                "pseudo": pseudo_dest,
                "port": port_num
            }
        }

    # @classmethod
    # def sock_server(cls, ip, port):
    #     pass

# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port = 5005
#     BUFFER_SIZE = 1024
#     msg = 'MDRRRRRRRRRRRRRRRRRRRRRRRRR'
#
#     Client.sock_server(ip, port)
#     # Client.connect(ip, port)
#     Client.sendmsg(msg)
#     datam = Client.recv(BUFFER_SIZE)
#     Client.close()
#     print("received data : ", datam)

