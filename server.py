import socket
import threading

server = socket.socket()
port = 9999
ip = '127.0.0.1'
server.bind((ip, port))
server.listen()
clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

def client_control(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast(message)
        except:
            index = clients.index(client)
            broadcast('{} was disconnected', format(names[index]))
            clients.remove(client)
            names.remove(names[index])
            client.close()
            break

def start_server():
    while True:
        client, address = server.accept()
        client.send('enter your name:'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        client_control_thread = threading.Thread(target=client_control, args=(client,))
        client_control_thread.start()
