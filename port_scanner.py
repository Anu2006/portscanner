from threading import Thread
from colorama import Fore
import asyncio
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.setdefaulttimeout(1)

host = '192.168.1.4'
num_of_ports = 1024
port = 445

async def port_scanner(port):
    try:
        sock.connect(port)
        return True

    except:
        return False
    # if sock.connect_ex((host, port)):
        # return Fore.RED + f'Port {port} of host {host} is closed'
    #
    # else:
    #     return Fore.GREEN + f'Port {port} of host {host} is opened'

async def main():
    for port in range(num_of_ports):
        res = await port_scanner(139)
        if res:
            print(Fore.GREEN + f'Port {port} of host {host} is opened')

        else:
            print(Fore.RED + f'Port {port} of host {host} is closed')

        print(Fore.WHITE, end='')
        # t = Thread(target=port_scanner, args=(i,))
        # t.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
