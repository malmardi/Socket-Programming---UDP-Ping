from datetime import datetime
from socket import *



clientSocket = socket(AF_INET,SOCK_DGRAM)


message='Ping'
counter = 10 # we need to send 10 pings
i = 0 # this counter is for the pings

success=0
loss=0
rtt_sum=0
minimum=10000000000
maximum=0
sequence_number=0

while i < counter:

    i+= 1


    send_Time = datetime.now()
    message2=( (str(sequence_number) + '\t' + str(send_Time))+ '\t' +message )
    clientSocket.sendto(message2.encode(),('localhost',12000))
    clientSocket.settimeout(1)

    try:

        reply,serverAddress = clientSocket.recvfrom(1024)
        success += 1
        receive_time = datetime.now()
        rtt = receive_time-send_Time


        print (reply.decode(),'RTT =',rtt.microseconds,'ms')
        sequence_number+=1

    except timeout:
        print ('Request timed out')

clientSocket.close()




