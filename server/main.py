import socket
from threading import Thread
from player import Player
wait=[]
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('127.0.0.1',12335))
listener.listen(1000)
socket.allow_reuse_adress=True
class Server(Thread):
    def __init__(self,player):
        super(Server,self).__init__()
        self.player = player
    def run(self):
        while True:
            try:
                print("Server started")
                self.player.process_msg()
            except Exception:
                # exit(0)
                break
while True:
    try:
        connect=listener.accept()
        print('connection success')
        Server(Player(connect[0],wait)).start()
    except Exception:
        break
# connect.close()
        # exit(0)

