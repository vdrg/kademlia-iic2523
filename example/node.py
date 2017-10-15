import socket
import logging
import sys
import os
import asyncio

from kademlia_iic2523.server import Server

PORT = sys.argv[1] # Este puerto será único para cada alumno
initialNodes = [("127.0.0.1", 8468)] # IP/PUERTO del servidor inicial
    
# Pueden descomentar la línea siguiente para obtener más información sobre las operaciones
#logging.basicConfig(level=logging.DEBUG)

# PARTE IMPORTANTE
async def runCommand(node, command):
    commands = command.split(" ")
    if (commands[0] == "get"):
        print("BEFORE")
        result = await node.get(commands[1])
        return result if result else "Not found."
    elif (commands[0] == "set"):
        # Guardará el valor en "command[2]" para la llave en "command[1]"
        success = await node.set(commands[1], commands[2])
        if (success):
            print("Value set.")
        else:
            print("There was an error setting the value")

loop = asyncio.get_event_loop()
#loop.set_debug(True)

server = Server()
server.listen(PORT, runCommand)
print("Listening at port", PORT) 
loop.run_until_complete(server.bootstrap(initialNodes))

try:
    loop.run_forever()
except Exception as e:
    print(e)
finally:
    print("Closing node")
    server.stop()
    loop.close()
