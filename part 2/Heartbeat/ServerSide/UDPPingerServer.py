# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
from datetime import datetime
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
received_packets_counter=0
lost_packets_counter=0
last_heartbeat_time=0
while True:
    try:
        serverSocket.settimeout(30)
        #Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        message_list = message.decode().split('\t')
        snd_Time = datetime.strptime(message_list[1],"%Y-%m-%d %H:%M:%S.%f")
        received_packets_counter+=1
        word=message_list[2].upper()
        print('Sequence Number', message_list[0])
        rec_Time = datetime.now()
        delay = rec_Time.microsecond - snd_Time.microsecond
        last_heartbeat_time = rec_Time
        # Capitalize the message from the client
        message = message.upper()
        #If rand is less than 4, we consider the packet lost and do not respond
        if rand < 4:
            lost_packets_counter+=1
            print('packet lost')
            continue
        # Otherwise, the server responds
        message = 'message modified('+word+") delay = " + str(delay) + ", Packets lost  = " + str(lost_packets_counter)
        serverSocket.sendto(message.encode(), address)
        print('Response delay =', delay)
    except timeout:
        print('Request timed out (Client considered dead after 3o sec)')