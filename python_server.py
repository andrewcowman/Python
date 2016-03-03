from socket import *
from thread import *

def getinfo(connectionSocket, data, addr):
    first_line = data.split('\n')[0]

    url = first_line.split(' ')[1]

    start = url.find("://")
    if(start == -1):
        domain = url
    else:
        domain = url[(url.find("://")+3):]

    port_position = domain.find(":")

    ending = domain.find("/")
    if ending == -1:
        ending = len(domain)

    server = ""

    port = -1

    if(port_position == -1 or ending < port_position):
        port = 80
        server = domain[:ending]
    else:
        port = int((domain[(port_position+1):])[:ending-port_position-1])
        server = domain[:port_position]

    sendtoserv(server, port, connectionSocket, data, addr)

def sendtoserv(host, port, connectionSocket, data, addr):
    print("Connecting to")
    print(host)
    print(port)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    print("Connected!")
    sock.send(data)

    while 1:
        response = sock.recv(4096)
        if(len(response) > 0):
            connectionSocket.send(response)
        else:
            break

    sock.close()
    connectionSocket.close()

            

        

serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(10)

print("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(4096)
    start_new_thread(getinfo, (connectionSocket, data, addr))
serverSocket.close()
