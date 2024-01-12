from socket import *

host = "localhost"
port = 777
addr = (host, port)

udp_soket = socket(AF_INET, SOCK_DGRAM)
udp_soket.bind(addr)

while True:
    q = input('Do you want to quit? y\\n: ')
    if q == "y": break

    print("wait data...")
    conn, addr = udp_soket.recvfrom(1024)
    print("client addres: ", addr)
    udp_soket.sendto(b"message received by the server", addr)

udp_soket.close()