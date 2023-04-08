# from scapy.all import *
# import pandas as pd
# from sklearn.cluster import AgglomerativeClustering
# from scipy.cluster import hierarchy
# import pandas as pd

# BIT_SPLIT = 4
# MAX_PAYLOAD = 10

# # Define a function to capture TCP packets until the connection is closed


# def capture_tcp_packets(ip_address, port):
#     # Create an empty list to store packet information
#     packets = []

#     # Set the flag variable to True initially
#     connection_open = True

#     # Define a function to append packet information to the packets list
#     def store_packet(packet):
#         #print("Sniffing")
#         nonlocal connection_open
#         if packet[TCP].payload:
#             #print(packet[TCP].flags)
#             # Extract TCP sequence number and packet arrival time
#             seq_num = packet[TCP].seq
#             arrival_time = packet.time

#             # Append packet information to the packets list
#             packets.append({'Sequence Number': seq_num,
#                            'Arrival Time': arrival_time})
#             print("len:", len(packets))

#         # Check for the TCP FIN flag to detect when the connection is closed
#         elif 'F' in packet[TCP].flags:
#             # Set the flag variable to False to stop capturing packets
#             print("FIN")
#             connection_open = False
#     filt = "tcp and dst port "+str(port)

#     # Use Scapy's sniff() function to capture packets until the connection is closed
#     sniff(prn=store_packet,
#           filter=filt, stop_filter=lambda p: not connection_open)

#     # Create a Pandas data frame from the packets list
#     df = pd.DataFrame(packets)

#     X = df['Arrival Time'].values.reshape(-1, 1)



#     # Initialize the AgglomerativeClustering model
#     agg_clustering = AgglomerativeClustering(
#         n_clusters=None, linkage='ward', distance_threshold=5)

#     # Fit the model to the data
#     agg_clustering.fit(X)

#     # Add the cluster labels as a new column in the dataframe
#     df['cluster_label'] = agg_clustering.labels_

#     index_l = 0
#     index_u = 0
#     message = ""
#     while index_u <= len(df)-1:
#         while index_u < len(df)-1 and df['cluster_label'][index_l] == df['cluster_label'][index_u + 1]:
#             index_u += 1
#         data = int(((df['Sequence Number'][index_u] -
#                     df['Sequence Number'][index_l])/MAX_PAYLOAD)+1)-1
#         # print(data)
#         binary_string = bin(data)[2:]
#         # print(binary_string)
#         if len(binary_string) < BIT_SPLIT:
#             binary_string = "0"*(BIT_SPLIT-len(binary_string) %
#                                  BIT_SPLIT) + binary_string
#         # print(binary_string+"\n")

#         message = message+binary_string
#         index_l = index_u+1
#         index_u = index_u+1

#     # calculate the number of bytes needed to represent the integer
#     num = int(message, 2)

#     # calculate the number of bytes needed to represent the integer
#     num_bytes = (len(message) + 7) // 8

#     # convert the integer to bytes
#     bytes_data = num.to_bytes(num_bytes, byteorder='big')

#     # Write to file
#     f = open("msg.txt", "w")
#     f.write(bytes_data.decode('utf-8'))
#     print("Message Received")

#     return df

from scapy.all import *
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
import pandas as pd

BIT_SPLIT = 4
MAX_PAYLOAD = 10

# Define a function to capture TCP packets until the connection is closed


def capture_tcp_packets(ip_address, port):
    # Create an empty list to store packet information
    packets = []

    # Set the flag variable to True initially
    connection_open = True

    # Define a function to append packet information to the packets list
    def store_packet(packet):
        #print("Sniffing")
        nonlocal connection_open
        if packet[TCP].payload:
            #print(packet[TCP].flags)
            # Extract TCP sequence number and packet arrival time
            seq_num = packet[TCP].seq
            arrival_time = packet.time

            # Append packet information to the packets list
            packets.append({'Sequence Number': seq_num,
                           'Arrival Time': arrival_time})
            print("len:", len(packets))

        # Check for the TCP FIN flag to detect when the connection is closed
        elif 'F' in packet[TCP].flags:
            # Set the flag variable to False to stop capturing packets
            print("FIN")
            connection_open = False
    filt = "tcp and dst port "+str(port)

    # Use Scapy's sniff() function to capture packets until the connection is closed
    sniff(prn=store_packet,
          filter=filt, stop_filter=lambda p: not connection_open)

    # Create a Pandas data frame from the packets list
    df = pd.DataFrame(packets)

    X = df['Arrival Time'].values.reshape(-1, 1)



    # Initialize the AgglomerativeClustering model
    agg_clustering = AgglomerativeClustering(
        n_clusters=None, linkage='ward', distance_threshold=5) #increase threshold if bitsplit increases

    # Fit the model to the data
    agg_clustering.fit(X)

    # Add the cluster labels as a new column in the dataframe
    df['cluster_label'] = agg_clustering.labels_

    index_l = 0
    index_u = 0
    message = ""
    while index_u <= len(df)-1:
        while index_u < len(df)-1 and df['cluster_label'][index_l] == df['cluster_label'][index_u + 1]:
            index_u += 1
        data = int(((df['Sequence Number'][index_u] -
                    df['Sequence Number'][index_l])/MAX_PAYLOAD)+1)-1
        # print(data)
        binary_string = bin(data)[2:]
        # print(binary_string)
        if len(binary_string) < BIT_SPLIT:
            binary_string = "0"*(BIT_SPLIT-len(binary_string) %
                                 BIT_SPLIT) + binary_string
        # print(binary_string+"\n")

        message = message+binary_string
        index_l = index_u+1
        index_u = index_u+1
    print("message len:",n)
    while n>8 and n%8!=0:
       print("inloop",n)
       print(message)
       message=message[1:]
       n -=1

    # calculate the number of bytes needed to represent the integer
    num = int(message, 2)

    # calculate the number of bytes needed to represent the integer
    num_bytes = (len(message) + 7) // 8

    # convert the integer to bytes
    bytes_data = num.to_bytes(num_bytes, byteorder='big')

    # Making bitstring valid in case it is not a multiple of 8
    
    print("Final bits",message)
    #Writing to file
    f = open("msg.txt", "w")
    f.write(bytes_data.decode('utf-8'))
    print("Message Received")

    return df

