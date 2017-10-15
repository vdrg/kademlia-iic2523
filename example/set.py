from kademlia_iic2523.ipc import ipcSend
import sys

ipcSend("set " + sys.argv[1] + " " + sys.argv[2])
#  if os.path.exists(".ipc"):
    #  client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    #  client.connect(".ipc")

    #  client.send(("set " + sys.argv[1] + " " + sys.argv[2]).encode("utf-8"))
    #  client.close()
#  else:
    #  print("Couldn't Connect!")
