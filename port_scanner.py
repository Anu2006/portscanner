from threading import Thread
from colorama import Fore
import socket

host = '192.168.0.1'
ports = 1024

socket.setdefaulttimeout(0.3)

def port_scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((host, port)):
        print(Fore.RED + f'\nport {port} is closed', end='')
        # return

    else:
        print(Fore.GREEN + f'\nport {port} is opened', end='')


def main():
    for port in range(1, ports + 1):
        t = Thread(target=port_scanner, args=(port,))
        t.start()


if __name__ == '__main__':
    main()
