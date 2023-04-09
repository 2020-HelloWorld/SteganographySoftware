from scapy.all import *
SERVER_IP = '192.168.120.18'
SERVER_PORT = 1234


def comm():

    # Simulating TCP 3-way handshake
    import socket

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to a remote server
    server_address = ('10.0.2.246', 1234)
    # client_socket.connect(server_address)

   # Send the ACK packet
   # send(ack_packet)

    with open('tosend.txt', 'rb') as f:
        file_bytes = bytearray(f.read())
        bits = ''.join(format(byte, '08b') for byte in file_bytes)
        print(bits)
    n = len(bits)
    print(n)
    i = 0
    ip_packet = IP(dst=SERVER_IP)
    print("HI")
# Create an ICMP packet with payload "10"
    # icmp_packet = UDP(dport=1234) / Raw(load=str(n))

    # Combine the IP and ICMP packets
    # packet = ip_packet / icmp_packet
    # client_socket.send("0".encode())
    source_port = 56099

    packet = IP(dst=SERVER_IP)/TCP(sport=1230, dport=SERVER_PORT,
                                   seq=0, ack=1, flags="PA", options=[('Timestamp', (0, 0))])/str(n)
    # Send the packet
    send(packet)
    time.sleep(2)
    seq_num = 1

    ack_num = 1

    while i < n:

        t = int(time.time())

        while t % 2 != int(bits[i]):
            t = int(time.time())
            # print("hi")
        packet = IP(dst=SERVER_IP)/TCP(sport=source_port, dport=SERVER_PORT,
                                       seq=seq_num, ack=ack_num, flags="PA", options=[('Timestamp', (t, 0))])
        i += 1

        print(packet[TCP].seq)
    #     # Receive the server's response
        send(packet)

    #     # Extract the new sequence number and acknowledge number from the server's response
        seq_num = seq_num+5
    #     ack_num = 1
        time.sleep(000000.1)

    # Send the packet with timestamp option
comm()
