from kademlia.network import Server as KademliaServer
from kademlia_iic2523.ipc import ipcListen
import asyncio
import os

class Server(KademliaServer):

    def __init__(self):
        super().__init__()

        self.ipcTask = None

        if os.path.isfile(".state"):
            with open(fname, 'rb') as f:
                data = pickle.load(f)
            self.ksize = data['ksize']
            self.alpha = data['alpha']
            self.id = data['id']
            if len(data['neighbors']) > 0:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.bootstrap(data['neighbors']))

    def listen(self, port, ipcCallback):
        super().listen(port)

        self.ipcTask = asyncio.ensure_future(ipcListen(lambda x: ipcCallback(self, x)))
        #asyncio.ensure_future(super().saveStateRegularly(".ipc"))

    def stop(self):
        super().stop()
        if self.ipcTask is not None:
            self.ipcTask.cancel()


