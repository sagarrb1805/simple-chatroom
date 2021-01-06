import threading
import socket

client = socket.socket()
client.connect(('127.0.0.1', 9999))

client_name = input('enter your name: ')


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'enter your name:':
                client.send(client_name.encode('ascii'))
            else:
                print(message)
        except:
            print('some error occured')
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(client_name, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()





