from time import perf_counter
from typing import List
import numpy as np

def open_file():
    l = ''
    with open('input16.txt') as f:
        lines = f.readlines()
        l = lines[0]
    return l 


def part1(data):
    binary_bits = hex_to_binary(data)
    
    label = get_label(binary_bits)

    find_version_score(binary_bits, label)


def find_version_score(binary_bits, label):
    score = []
    score_value = ''
    for index, char in enumerate(label):
        if char == 'V':
            score_value += binary_bits[index]
        if char != 'V' and score_value != '':
            score.append(score_value)
            score_value = ''

    total_score = 0        
    for version_score in score:
        total_score += int(version_score, 2)
    
    print(f"Version score = {total_score}")


def part2(data):
    # binary_bits = hex_to_binary('9C0141080250320F1802104A08')
    binary_bits = hex_to_binary(data)

    label = get_label(binary_bits)
    format_label_and_binary_bits2(label, binary_bits)
    

    



def find_packets(label, binary_bits):
    packet_labels = []
    packet_bits = []
    packet_label = ''
    packet_bit = ''

    for index, char in enumerate(label):
        if char == 'V' and len(packet_label) > 5:
            packet_labels.append(packet_label)
            packet_bits.append(packet_bit)
            packet_label = ''
            packet_bit = ''
        if index < len(binary_bits):
            packet_bit += binary_bits[index]
        packet_label += char
    packet_labels.append(packet_label)
    packet_bits.append(packet_bit)
    return packet_labels, packet_bits

def format_label_and_binary_bits(label, binary_bits):
    packet_labels, packet_bits = find_packets(label, binary_bits)

    #print(packet_labels)
    #print(packet_bits)

    new_packet_labels = []
    new_packet_bits = []

    for index, packet in enumerate(packet_labels):
        if packet[-1] == 'L':
            new_packet_labels.append([packet])
            new_packet_bits.append([packet_bits[index]])
        else:
            new_packet_labels[-1].append(packet)
            new_packet_bits[-1].append(packet_bits[index])
    
    for packet in new_packet_labels:
        packet.reverse()
    
    for packet in new_packet_bits:
        packet.reverse()
    
    new_packet_labels.reverse()
    new_packet_bits.reverse()
    
    print(new_packet_labels)
    print(new_packet_bits)



def format_label_and_binary_bits2(label, binary_bits):
    packet_labels, packet_bits = find_packets(label, binary_bits)

    packet_labels.reverse()
    packet_bits.reverse()

    values = []
    values_prev = []

    for index, packet in enumerate(packet_labels):
        print(values)
        print(values_prev)
        type_id = packet_bits[index][3:6]
        type_id_int = int(type_id, 2)

        if type_id_int > 4 and len(values) == 0 and len(values_prev) != 0:
            new_values = [values_prev[-1][-1], values_prev[-2][-1]]
            value = decode_transmission(packet, packet_bits, index, new_values, type_id_int)
            values.append(value)
        
        else:
            value = decode_transmission(packet, packet_bits, index, values, type_id_int)

            if type_id_int == 4:
                values.append(value)
            
            else:
                values.append(value)
                values_prev.append(values)
                values = []

    values_prev.append(values)
    print(values_prev)

def decode_transmission(packet, packet_bits, index, values, type_id_int):    
    if type_id_int == 4:
        value = find_literal_score_for_one_packet(packet, packet_bits[index])

    elif type_id_int == 0:
        value = sum(values)

    elif type_id_int == 1:
        value = np.prod(values)
    
    elif type_id_int == 2:
        value = min(values)

    elif type_id_int == 3:
        value = max(values)
    
    elif type_id_int == 5:
        value = 1 if values[-1] > values[-2] else 0
    
    elif type_id_int == 6:
        value = 1 if values[-1] < values[-2] else 0
    
    elif type_id_int == 7:
        value = 1 if values[-1] == values[-2] else 0
    
    return value



def find_value_of_outermost_packet(label, binary_bits):





    for index, packet in enumerate(packet_labels):
        type_id = packet_bits[index][3:6]
        type_id_int = int(type_id, 2)

        if type_id_int == 4:
            value = find_literal_score_for_one_packet(packet, packet_bits[index])

        elif type_id_int == 0:
            value = sum(values)

        elif type_id_int == 1:
            value = np.prod(values)
        
        elif type_id_int == 2:
            value = min(values)

        elif type_id_int == 3:
            value = max(values)
        
        elif type_id_int == 5:
            value = 1 if values[-1] > values[-2] else 0
        
        elif type_id_int == 6:
            value = 1 if values[-1] < values[-2] else 0
        
        elif type_id_int == 7:
            value = 1 if values[-1] == values[-2] else 0
        
        values.append(value)

    print(f"Value of outermost packet = {values[-1]}")
    
def find_literal_score_for_one_packet(packet_label, packet_bit):
    
    looking_for = 'A'
    number = ''
    for index, char in enumerate(packet_label):
        if char == looking_for:
            looking_for = chr(ord(looking_for) + 1)
        elif index < 6:
            pass
        else:
            number += packet_bit[index]
    return int(number, 2)



    

    


def get_label(binary_bits):
    if len(binary_bits) < 11:
        return ''
    type_of_next_packet = find_next_packet_type(binary_bits)
    label = ''
    if type_of_next_packet == 'literal':
        label = find_literal(binary_bits)
    
    elif type_of_next_packet == 'operator_15':
        label = find_operator_15(binary_bits)

    elif type_of_next_packet == 'operator_11':
        label = find_operator_11(binary_bits)

    return label


def find_operator_15(binary_bits):
    label = 'VVVTTTILLLLLLLLLLLLLLL'
    total_length_in_bits = binary_bits[7:22]
    total_length_int = int(total_length_in_bits, 2)

    reading = True
    start = 22
    end = start + total_length_int
    
    new_label = ''
    while reading:
        x = get_label(binary_bits[start:end])
        new_label += x
        start += len(new_label)
        
        if start > end or x == '':
            reading = False

    label += new_label
    return label


def find_operator_11(binary_bits):
    label = 'VVVTTTILLLLLLLLLLL'
    num_of_sub_packets_in_bits = binary_bits[7:18]
    num_of_sub_packets_int = int(num_of_sub_packets_in_bits, 2)
    
    for i in range(num_of_sub_packets_int):
        label += get_label(binary_bits[len(label):])

    return label


def find_literal(binary_bits):
    label = 'VVVTTT'
    char = 'A'
    reading = True
    while reading:
        if binary_bits[len(label)] == '0':
            reading = False
        label += char * 5
        char = chr(ord(char) + 1)
    return label
    

def find_next_packet_type(binary_bits):
    type_id = binary_bits[3:6]
    type_id_int = int(type_id, 2)

    if type_id_int == 4:
        return 'literal'
    
    length_type_id = binary_bits[6]
    
    if length_type_id == '0':
        return 'operator_15'
    return 'operator_11'


def hex_to_binary(hex):
    hex_to_bin_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    
    binary_string = ''
    for char in hex:
        binary_string += hex_to_bin_dict[char]
    return binary_string
    

def main():
    start = perf_counter()
    data = open_file()
    
    # my function here
    part2(data)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()