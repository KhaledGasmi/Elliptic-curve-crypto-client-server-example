from scapy.all import sniff, TCP

def packet_callback(packet):
    if TCP in packet and packet[TCP].payload:
        print("\n[+] Encrypted Packet:")
        print(packet.show(dump=True))

# Start sniffing on the loopback interface
sniff(prn=packet_callback, store=0, iface="lo", filter="tcp port 5000")
