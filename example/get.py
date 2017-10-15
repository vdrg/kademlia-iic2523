from kademlia_iic2523.ipc import ipcSend
import sys

def onResponse(message):
    print(message)

ipcSend("get " + sys.argv[1], onResponse)
#  if os.path.exists(".ipc"):
    #  client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    #  client.connect(".ipc")

    #  client.send(("get " + sys.argv[1]).encode("utf-8"))

    #  datagram = client.recv(1024)
    #  if datagram:
        #  print(datagram.decode("utf-8"))
    #  client.close()
#  else:
    #  print("Couldn't Connect!")
