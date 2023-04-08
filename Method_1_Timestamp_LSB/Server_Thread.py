from scapy.all import *

# Define server address and port
SERVER_HOST = '0.0.0.0' #<Interface IP>
SERVER_PORT = 1234

# Define a function to handle incoming packets
n = []
i=0

def handle_packet1(packet):
	if ICMP in packet and packet.payload:
		#global n
		n.append(int(packet.payload.load))
		print("Incoming data len:", n)





bits=[]


sniff(filter='icmp', prn=handle_packet1,count=1)
print("Waiting for",n[0],"packets")


    
def handle_packet(packet):

    # Check if TCP Timestamp option is present
    if TCP in packet and packet[TCP].options:
        tcp_fields = packet[TCP].fields
        for option in tcp_fields['options']:
            if option[0] == 'Timestamp':
                timestamp_value = option[1]
                print("TCP Timestamp:", timestamp_value)
                bits.append(str(timestamp_value[0]%2))
                print("Bits Received",len(bits))

# Start sniffing for incoming packets
sniff(filter='(tcp dst port 1234)', prn=handle_packet,count=n[0])

#Create Bitstring
bitstring="".join(bits)
num = int(bitstring, 2)

# calculate the number of bytes needed to represent the integer
num_bytes = (len(bitstring) + 7) // 8

# convert the integer to bytes
bytes_data = num.to_bytes(num_bytes, byteorder='big')


#Write to file
f=open("msg.txt","w")
f.write(bytes_data.decode('utf-8'))


