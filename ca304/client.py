import socket

def myclient():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myIPaddress = '127.0.0.1'
    myPort = 8000
    mysocket.connect((myIPaddress, myPort))
    data = input('>> ')
    #keep sending data until the word 'bye' is encountered
    #if so, close the socket
    while data.lower().strip() != 'bye':
        mysocket.send(data.encode())
        message = mysocket.recv(1024).decode()
        print('>> Server: ' + str(message))
        data = input('>> ')
    mysocket.close()

if __name__ == '__main__':
    myclient()