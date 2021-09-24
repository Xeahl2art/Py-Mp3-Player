import socket
server   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def mysend(frame):
    server.sendto(frame, ("127.0.0.1",1237))

