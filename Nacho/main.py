from client import *

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 6009
    BUFFER_SIZE = 1024

    s = Client()
    s.connclient(ip, port)
    print("Connexion établie avec le serveur sur le port {}".format(port))

    msg_to_send = b""
    while msg_to_send != "logout":
        msg_to_send = input("> ")
        s.sendmsg(msg_to_send)
        datam = s.sock_server.recv(BUFFER_SIZE)
        print(datam)

    print("Fermeture de la connexion")
    s.sock_server.close()
