#!/usr/bin/env python


from scapy.all import *
# Set the GET request
get='GET / HTTP/1.0\n\n'
# Set your target
ip=IP(dst="www.google.com")
# Create a random source port (not needed but nice to have)
port=RandNum(1024,65535)
# Create SYN packet
SYN=ip/TCP(sport=port, dport=80, flags="S", seq=42)
# Send SYN and receive SYN,ACK
SYNACK=sr1(SYN)
# Create ACK with GET request
ACK=ip/TCP(sport=SYNACK.dport, dport=80, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1) / get
# SEND our ACK-GET request
reply,error=sr(ACK)
# Print the reply
print(reply.show())
