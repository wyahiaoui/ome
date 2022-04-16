from modules import interface, caputre
from modules.server import run_server
from threading import Thread

def write_file(filename, data):
    with open(filename, "w") as file1:
        file1.write(str(data))

if __name__ == "__main__":
    network = interface.NetworkInterface()
    thread = Thread(target = run_server)
    thread.start()
    active_interface = network.getActiveInterfaceConnection()
    current_ip = network.getIp()
    print('active internet interface is: ' + active_interface + ", ip: " + current_ip)
    shark_agent = caputre.sharkCapture(active_interface).live_capture(current_ip)

