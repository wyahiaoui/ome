from modules import interface, caputre

def write_file(filename, data):
    with open(filename, "w") as file1:
        file1.write(str(data))

if __name__ == "__main__":
    network = interface.NetworkInterface()
    active_interface = network.getActiveInterfaceConnection()
    current_ip = network.getIp()
    print('active internet interface is: ' + active_interface + ", ip: " + current_ip)
    shark_agent = caputre.sharkCapture(active_interface).live_capture(current_ip)

