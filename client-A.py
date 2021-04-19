import threading
import os
import socket
os.system('tput setaf 2')
print("""
                    ----------------------------------------
                         !!  ARTH PYTHON CHAT PROGRAM !!
                    ----------------------------------------
        """)

os.system('tput setaf 4')
def receive():
    s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM )
    s.bind(("192.168.43.108",2345))
    while True:
        x = s.recvfrom(5000)
        y = x[0].decode()
        sender_ip = x[1][0]
        os.system('tput setaf 6')
        print("""
                                    receive {0}: {1}\n""".format(sender_ip,y))
        os.system('tput setaf 3')


#ip = input("Receiver IP: ")
#port = int(input("Receiver port: "))

def send():
    s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM )
    while True:
        #msg = input()
        os.system("tput setaf 4")
        x = s.sendto(input("sender 192.168.43.108: ").encode(),('192.168.43.190',1234))
        os.system("tput setaf 2")


send1 = threading.Thread( target=send )
receive1 = threading.Thread( target=receive )

send1.start()
receive1.start()
