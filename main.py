from modules import interface, caputre
import pyshark

def write_file(filename, data):
    with open(filename, "w") as file1:
        file1.write(str(data))

network = interface.NetworkInterface()
print(network.getIp())
active_interface = network.getActiveInterfaceConnection()
print('active internet interface is: ' + active_interface)
shark_agent = caputre.sharkCapture(active_interface).live_capture(network.getIp())

