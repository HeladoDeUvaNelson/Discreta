import os
from dotenv import load_dotenv
load_dotenv()

import socket

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))


def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        print(f"Received {data!r}")