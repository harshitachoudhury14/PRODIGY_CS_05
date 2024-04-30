import scapy.all as scapy

def packet_callback(packet):
    destination_ip = packet[1].dst
    protocol = packet[1].proto

    if packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")

print("Starting packet sniffer...")
scapy.sniff(iface="Ethernet", prn=packet_callback, store=False)
