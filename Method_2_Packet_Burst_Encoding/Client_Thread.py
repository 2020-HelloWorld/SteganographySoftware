import socket
from scapy.all import *
SERVER_IP = '10.0.2.246'
SERVER_PORT = 1234
MAX_PAYLOAD = 10  # BYTES
BIT_SPLIT = 4
MAX_PACKETS = 2**4


# create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set the IP address and port number of the server
server_address = (SERVER_IP, 1234)

print('Connecting to {server_address}...')


def method2():
    # connect to the server
    try:
        client_socket.connect(server_address)

    except Exception as e:
        print("Connection failed:",e)
        return
    i = 0
    with open('tosend.txt', 'rb') as f:
        file_bytes = bytearray(f.read())
        bits = ''.join(format(byte, '08b') for byte in file_bytes)
        print(bits)
    n = len(bits)
    print("datalen:", n)
    # to make it divisible by BIT_SPLIT
    padding = n % BIT_SPLIT
    if padding != 0:
        bits = "0"*(BIT_SPLIT-padding)+bits
        n += BIT_SPLIT-padding
    print("modified datalen:", n)
    print("modified bits:",bits)
    # bitstring = bits
    # num = int(bitstring, 2)


# calculate the number of bytes needed to represent the integer
    # num_bytes = (len(bitstring) + 7) // 8

    # # convert the integer to bytes
    # bytes_data = num.to_bytes(num_bytes, byteorder='big')
    # print(bytes_data.decode())

    try:
        message = "0"*MAX_PAYLOAD
        enc = message.encode()
        j = BIT_SPLIT
        g=0
        while i < n:
            # send data to the server
            numOfPackets = int(bits[i:i+j], 2)+1
            # print(numOfPackets, ":", bits[i:i+j])
            print(numOfPackets)
            g+=numOfPackets
            
            for p in range(numOfPackets):
                time.sleep(0.1)
            
                
                client_socket.sendall(enc)
            print("No.of packets sent:",g)
            time.sleep(5)
            
            

            i = i+j
            print(i)
        print("Transfer Successful")
        #client_socket.sendall("bye".encode())
        client_socket.close()
    except Exception as e:
        client_socket.close()
        print(e)
        return


# finally:
#     # close the socket
#     client_socket.close()
method2()
