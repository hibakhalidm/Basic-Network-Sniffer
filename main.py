from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw
from scapy.all import sniff


def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"IP: {ip_src} -> {ip_dst} | TCP: {tcp_sport} -> {tcp_dport}")

            if Raw in packet:
                payload = packet[Raw].load
                print(f"  Payload: {payload[:100]}")  # Print the first 100 bytes of the payload

        elif protocol == 17:  # UDP
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"IP: {ip_src} -> {ip_dst} | UDP: {udp_sport} -> {udp_dport}")


sniff(prn=packet_callback, store=0)

# Analyse captured Data
from collections import Counter

packet_counts = Counter()


def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        packet_counts[protocol] += 1

        print(f"IP Packet: {ip_src} -> {ip_dst} | Protocol: {protocol}")
        if TCP in packet:
            print(f"  TCP Packet: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"  UDP Packet: {packet[UDP].sport} -> {packet[UDP].dport}")

    print(f"Packet Counts: {packet_counts}")


sniff(prn=packet_callback, store=0)
#save captured data to a file
import csv

with open('captured_packets.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Source IP', 'Destination IP', 'Protocol', 'Source Port', 'Destination Port'])


    def packet_callback(packet):
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = packet[IP].proto
            row = [ip_src, ip_dst, protocol, '', '']

            if TCP in packet:
                row[3] = packet[TCP].sport
                row[4] = packet[TCP].dport
            elif UDP in packet:
                row[3] = packet[UDP].sport
                row[4] = packet[UDP].dport

            writer.writerow(row)
            print(f"Captured Packet: {row}")


    sniff(prn=packet_callback, store=0)
