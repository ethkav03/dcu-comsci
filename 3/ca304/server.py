import socket

def myserver():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myIPAddress = '127.0.0.1'
    myPort = 8000
    mysocket.bind((myIPAddress, myPort))
    mysocket.listen()
    print('I am listening...')
    connection, address = mysocket.accept()
    print('Connection from ' + str(address))
    while True:
        message = connection.recv(1024).decode()
        if not message:
            break
        print('>> Client: ' + str(message))
        data = input('>> ')
        connection.send(data.encode())    
    connection.close()

if __name__ == "__main__":
    myserver()