import pyshark

class sharkCapture:
    def __init__(self, active_interface) -> None:
        # pass
        self.capture = pyshark.LiveCapture(interface=active_interface)

    def get_packet_details(self, packet):
        print("incoming", packet)
        try: 
            packet_data = {}
            packet_data['protocol'] = packet.transport_layer
            packet_data['source_address'] = packet.ip.src
            packet_data['source_port'] = packet[packet.transport_layer].srcport
            packet_data['destination_address'] = packet.ip.dst
            packet_data['destination_port'] = packet[packet.transport_layer].dstport
            packet_data['packet_time'] = packet.sniff_time
            return packet_data
        except:
            print("packet is dammaged")
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
            if self.ip_class(packet_details['source_address']) or self.ip_class(packet_details['destination_address']):
                return packet_details
            print("address" + self.ip_class(packet_details['source_address']) + " sec: " + self.ip_class(packet_details['destination_address']))
        return None

    def live_capture(self):
        for raw_packet in self.capture.sniff_continuously():
            udp_traffic = self.filter_local_traffic(raw_packet, 'udp')
            if udp_traffic != None:
                # print(udp_traffic)
                pass