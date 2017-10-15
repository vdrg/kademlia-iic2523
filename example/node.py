import socket
import logging
import sys
import os
import asyncio

from kademlia_iic2523.server import Server

# Este puerto será único para cada alumno
PORT = sys.argv[1]

# IP/PUERTO del servidor inicial que estará corriendo en el clúster
initialNodes = [("127.0.0.1", 8468)] 
    
# Pueden descomentar la línea siguiente para obtener más información sobre las operaciones
#logging.basicConfig(level=logging.DEBUG)

# PARTE IMPORTANTE:
# Procesa los comandos recibidos por get.py y set.py
# Opcionalmente, retorna un string, que es enviada como respuesta
async def runCommand(node, message):
    command = message.split(" ")
    if (command[0] == "get"):
        # Consulta a la DHT por la llave recibida
        result = await node.get(command[1])

        # Si se encontraron valores, enviarlos de vuelta
        return result if result else "Not found."
    elif (command[0] == "set"):
        # Guardará el valor en "command[2]" con la llave en "command[1]"
        success = await node.set(command[1], command[2])
        if (success):
            print("Value set.")
        else:
            print("There was an error setting the value")

loop = asyncio.get_event_loop()
#loop.set_debug(True)

server = Server()
server.listen(PORT, runCommand)
print("Listening at port", PORT) 

# Conectarse al nodo inicial
loop.run_until_complete(server.bootstrap(initialNodes))

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    pass
finally:
    print("Closing node")
    server.stop()
    loop.close()
