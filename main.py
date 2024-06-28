from threading import Thread
from network.server import recv
from network.client import send
from cli.shell import shell

T_recv = Thread(target = recv, daemon=True)
T_send = Thread(target = send, daemon=True)
T_shell = Thread(target = shell)

T_recv.start()
# T_send.start()
T_shell.start()