import socket
import pickle

HEADERSIZE = 20
msglen = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1111))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""
