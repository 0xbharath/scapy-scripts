from __future__ import print_function
from sys import argv
from scapy.all import rdpcap, IP

def extract_machine_names(pcap):
    machines = []
    packets = rdpcap(pcap)
    for i in range(len(packets)):
             if packets[i][IP].src not in machines:
                 machines.append(packets[i][IP].src)
                 print(len(machines), packets[i][IP].src)
             elif packets[i][IP].dst not in machines:
                 machines.append(packets[i][IP].dst)
                 print(len(machines), packets[i][IP].dst)
    return machines

if __name__ == '__main__':
    pcap = argv[1]
    if len(argv) < 2:
        print("Usage: python all_devices.py path_to_pcap")
    print("\nList of all the machines in pcap =>", extract_machine_names(pcap),end="\n\n")
