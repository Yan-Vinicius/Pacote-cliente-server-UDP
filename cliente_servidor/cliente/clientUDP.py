import socket

def main():

    host = "localhost"
    port = 5433
    msg = "Olá"

    try:

        #socket para o protocolo UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("Cliente socket criado com sucesso")

    except socket.error as e:
        print("Conexão falhou!")
        print("Erro: {}" .format(e))

    try:
        print("Cliente " + msg)
        s.sendto(msg.encode(), (host, 5432))

        #recvfrom(numero de bytes)
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()


        print("Cliente: ", dados)

    except socket.error as e:
        print("Erro {}" .format(e))

    finally:

        print("Cliente: fechando a conexão")
        s.close()

if __name__ == '__main__':
    main()
