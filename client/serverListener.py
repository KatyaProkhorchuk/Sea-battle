from threading import Thread


class ServerListener(Thread):
    def __init__(self,controller,sock):
        Thread.__init__(self)
        self.controller = controller
        self.sock = sock
    def run(self):
        while True:
            try:
                sock_recv = self.sock.recv(256).decode('utf-8')
                arr = sock_recv.split('@')
                if sock_recv == '':
                   break
                for data in arr:
                    if data != '':
                        self.controller.update(data)
            except Exception:
                break
                