
from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet captured: {ip_src} -> {ip_dst}")
        
        if TCP in packet:
            print(f"TCP Packet: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Packet: {packet[UDP].sport} -> {packet[UDP].dport}")

def start_sniffing(interface):
    print(f"Starting packet capture on interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Replace 'eth0' with the appropriate network interface for your system
    interface = "eth0"  # You may need to change this to the correct interface
    start_sniffing(interface)
