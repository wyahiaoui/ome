import socket
import netifaces

class NetworkInterface: 
    def __init__(self):
        self.interfaces = self.getInterfaces()

    def getInterfaces(self):
        return netifaces.interfaces()

    def getInterfaceData(self, interName):
        return netifaces.ifaddresses(interName)

    def getInterfaceInetData(self, interName):
        interfaceData = self.getInterfaceData(interName)
        if netifaces.AF_INET in interfaceData:
            return interfaceData[netifaces.AF_INET]
        else: 
            return None

    def getIp(self):
        return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

    def getActiveInterfaceConnection(self):
        ip_address = self.getIp()
        for int in self.interfaces:
            netData = self.getInterfaceInetData(int)
            if netData != None: 
                if netData[0]['addr'] == ip_address:
                    return int
        return None
