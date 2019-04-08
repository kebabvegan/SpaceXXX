from socket import *
import sys
import datetime
import threading
import json

lockName = threading.Semaphore()
mapPseudo = {}


def addUser(pseudo, socket):
    lockName.acquire()
    mapPseudo[socket] = pseudo
    lockName.release()


def removeUser(socket):
    lockName.acquire()
    del mapPseudo[socket]
    lockName.release()


def traiter_client(socket_client):
    connected = True
    while connected:
        wrapper = socket_client.makefile()
        ligne = wrapper.readline()[:-1]
        print('ENVOYE PAR CLIENT')
        print(ligne)
        jsonData = json.loads(ligne)
        print(jsonData)

        message = 'error : unknown exchange'
        if jsonData["exchange"] == 'login':
            addUser(jsonData["pseudo"], sock_client)
            message = "{code : 200}"
            print(mapPseudo)
        if jsonData["exchange"] == "logout":
            removeUser(sock_client)
            message = "{code : 200}"
            print(mapPseudo)
        socket_client.send(message.encode())


def loadConfiguration():
    configuration = {}
    conf = open('spaceXserver.conf', 'r')
    for ligne in conf:
        currentLine = ligne
        currentLine.replace("\n", "")
        data = currentLine.split("=")
        configuration[data[0]] = data[1].replace("\n", "")
    return configuration


if __name__ == '__main__':
    conf = loadConfiguration()
    print(conf)
    sock_server = socket()  # TCP socket
    sock_server.bind(("", int(conf['port'])))
    print(f"Server listening on port : {conf['port']}")
    sock_server.listen(int(conf['client_number']))
    while True:
        try:
            sock_client, adr_client = sock_server.accept()
            print(f"Connection de {adr_client}")
            threading.Thread(target=traiter_client, args=(sock_client,)).start()
        except KeyboardInterrupt:
            break
    sock_server.shutdown(SHUT_RDWR)
    print('\nshutting down')
    for t in threading.enumerate():
        if t != threading.main_thread():
            t.join()
sys.exit(0)