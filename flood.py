from scapy.all import *
from random import randrange
from os import popen
import time

def main():
	sendpacket()
	
def sendpacket():
	destIP = "10.0.0.2"
	print destIP
	src_port = 80
	dst_port = 1
	interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()
	
	packet = Ether()/IP(dst=dstIP,src="10.0.0.1"))/UDP(dport=dst_port,sport=src_port)
	print(repr(packets))
	sendp(packets,iface=interface.rstrip)
	
main()