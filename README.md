# scapy-scripts
A collection of (crappy) scapy scripts, mostly scripts that I wrote for aiding in pen tests and security audits.

**all_devices_pcap.py**       - A script to extract all the IP addresses of endpoints in a PCAP.<br>
**arp_mitm.py**       - A script to perform ARP cache posioning(mitm).<br>
**cam_overflow.py**   - A script to perform classic CAM overflow attack to force Layer 2 switch into hub mode.<br>
**ipidseq.py**        - A script to check IP ID generation pattern. Takes an IP adress as command-line argument. <br>
**ipidscanner.py**    - A script to scan a victim through zombie. Takes a zombie IP, victim IP, victim port as arguments.<br>
**mail_sniffer.py**   - A script that sniffs SMTP traffic and prints the payload(used to sniff usernames & passwords on LAN).<br>
