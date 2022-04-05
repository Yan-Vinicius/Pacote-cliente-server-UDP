import socket


def serverUDP():

    host = "localhost"
    port = 5432

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("Socket criado com sucesso")

    except socket.error as e:

        print("Error na conexão com o socket: {}".format(e))

    try:

        s.bind((host, port))

        msgServer = "\nServer: conexão funcionando"

        while 1:

            dados, end = s.recvfrom(4096)

            if dados:
                print("Servidor enviando mensage...")
                s.sendto(dados + (msgServer.encode()), end)


    except socket.error as e:

        print("Erro na ligação cliente/server: {}".format(e))

serverUDP()