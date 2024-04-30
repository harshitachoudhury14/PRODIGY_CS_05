# PRODIGY_CS_05
Network Packet Analyzer Creating a packet sniffer tool involves capturing and analyzing network packets as they pass through a network interface. It's essential to use such tools ethically and legally, ensuring they are only used for educational purposes or with explicit consent.

Before running the code, ensure you have the scapy library installed (pip install scapy). This code sets up a packet sniffer using Scapy, a powerful packet manipulation tool. It captures packets on the specified network interface (eth0 in this example) and calls the packet_callback function for each captured packet.

The packet_callback function extracts relevant information such as source and destination IP addresses, protocol, and payload data (if available) from each packet and prints it to the console.

Remember, it's crucial to use packet sniffers responsibly and ethically. Unauthorized interception of network traffic may violate privacy laws and regulations. Always ensure that you have proper authorization or consent before using such tools, and avoid capturing sensitive information belonging to others.
