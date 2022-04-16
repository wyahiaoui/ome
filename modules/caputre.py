import pyshark
import requests

def get_geo(ip):
    r = requests.get("https://geolocation-db.com/json/" + ip)
    return r.text

class sharkCapture:
    def __init__(self, active_interface) -> None:
        # pass
        self.capture = pyshark.LiveCapture(interface=active_interface)

    def get_packet_details(self, packet):
        # print("incoming", packet)
        packet_data = {}
        try: 
            packet_data['protocol'] = packet.transport_layer
            packet_data['source_address'] = packet.ip.src
            packet_data['source_port'] = packet[packet.transport_layer].srcport
            packet_data['destination_address'] = packet.ip.dst
            packet_data['destination_port'] = packet[packet.transport_layer].dstport
            packet_data['packet_time'] = packet.sniff_time
            return packet_data
        except:
            print("packet is dammaged", packet_data)
            pass


    def filter_all_traffic_file(self, packet, protocolType):
        if hasattr(packet, protocolType):
            results = self.get_packet_details(packet)
            return results

    def ip_class(self, ip):
        addr = (int(ip.split('.')[0]) & 0x80) >> 6
        if (addr == 0b10):
            return True
        else:
            return False

    def filter_local_traffic(self, packet, protocolType):
        packet_details = self.filter_all_traffic_file(packet, protocolType)
        if packet_details != None:
            if self.ip_class(packet_details['source_address']) ^ self.ip_class(packet_details['destination_address']):
                return packet_details
            # print("address" + self.ip_class(packet_details['source_address']) + " sec: " + self.ip_class(packet_details['destination_address']))
        return None

    def live_capture(self, current_ip):
        captured = []
        for raw_packet in self.capture.sniff_continuously():
            udp_traffic = self.filter_local_traffic(raw_packet, 'udp')
            if udp_traffic != None:
                # print(udp_traffic)
                ip = ""
                if (udp_traffic["source_address"] == current_ip):
                    ip = udp_traffic["destination_address"]
                else:
                    ip = udp_traffic["source_address"]
                if not ip in captured:
                    print("geo", get_geo(ip))
                    captured += [ip]
                