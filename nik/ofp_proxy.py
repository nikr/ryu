# Copyright (C) 2014 Niklas Rehfeld (or maybe VUW or something.)

"""
This is a bit of a tricky one. On the one hand it is a server, as we need to listen to the controllers, but on the other hand it's a client, as we also need to pass on messages from the actual switch to the controller. 

hmmmm... what to use...

"""

import asyncore

class ProxyServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = ControllerHandler(sock)
    
class ControllerHandler(asyncore.dispatcher_with_send):
    def __init__(self,socket):
        pass

    def handle_read(self):
        pass


class ExternalController(object):
    def __init__(self, address):
        self._address = address
