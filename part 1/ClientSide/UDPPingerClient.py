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

while i < counter:

    i+= 1


    send_Time = datetime.now()
    clientSocket.sendto(message.encode(),('localhost',12000))
    clientSocket.settimeout(1)

    try:

        reply,serverAddress = clientSocket.recvfrom(1024)
        success += 1
        receive_time = datetime.now()
        rtt = receive_time-send_Time

        if rtt.microseconds>maximum:
            maximum=rtt.microseconds

        if rtt.microseconds<minimum:
            minimum=rtt.microseconds

        rtt_sum+=rtt.microseconds
        print ('Reply from Server: message=',reply.decode(),'RTT =',rtt.microseconds,'ms')
    except timeout:
        print ('Request timed out')
        loss+=1
clientSocket.close()
avg=rtt_sum/success

print('\nPing statistics')
print('Packets: Sent=',counter,', Received=', success,',Lost=',loss,'(',loss/10.0,'% loss)')
print('Approximate round trip times in milli-seconds:')
print('Minimum=', minimum/1000.0, ',Maximum=', maximum/1000.0, 'Average=', avg/1000.0)



