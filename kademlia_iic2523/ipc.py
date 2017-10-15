import socket
from asyncio import get_event_loop, CancelledError
import os
import sys

SOCKET_FILE = ".ipc"

async def ipcListen(callback):
    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)

    ipc = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    ipc.setblocking(False)
    ipc.bind(SOCKET_FILE)
    ipc.listen(2)

    loop = get_event_loop()

    print("Openened a unix socket...")

    sockAccept = None

    try:
        while True:
            sockAccept = loop.sock_accept(ipc)
            conn, addr = await sockAccept
            datagram = conn.recv(1024)
            if datagram:
                response = await callback(datagram.decode("utf-8"))
                if response:
                    conn.send(response.encode("utf-8"))
            conn.close()
    except CancelledError:
        pass
    finally:
        print("Shutting down...")
        if sockAccept is not None:
            #  sockAccept.set_exception(CancelledError)
            sockAccept.cancel()
        ipc.close()
        os.remove(SOCKET_FILE)

def ipcSend(message, callback=None):
    if os.path.exists(SOCKET_FILE):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(SOCKET_FILE)

        client.send(message.encode("utf-8"))

        if callback is not None:
            datagram = client.recv(1024)
            if datagram:
                callback(datagram.decode("utf-8"))
        client.close()
    else:
        print("Couldn't Connect!")