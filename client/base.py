class Base:
    def __init__(self, sock, controller, msg=''):
        self.sock = sock
        self.controller = controller
        self.msg = msg

    def draw(self,window):
        pass

    def remove(self,window):
        pass

    def update(self,*argc):
        pass
