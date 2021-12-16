from time import perf_counter
from typing import List

def open_file():
    l = ''
    with open('test_input16.txt') as f:
        lines = f.readlines()
        l = lines[0]
    return l 


def part1(data):
    #binary_bits = hex_to_binary(data)
    binary_bits = hex_to_binary('8A004A801A8002F478')
    print(binary_bits)
    label = get_label_based_on_bits(binary_bits)
    print(label)
    print("-----------------------------------------------------")

    binary_bits = hex_to_binary('620080001611562C8802118E34')
    label = get_label_based_on_bits(binary_bits)
    print(label)
    print("-----------------------------------------------------")

    binary_bits = hex_to_binary('C0015000016115A2E0802F182340')
    label = get_label_based_on_bits(binary_bits)
    print(label)
    print("-----------------------------------------------------")

    binary_bits = hex_to_binary('A0016C880162017C3686B18A3D4780')
    label = get_label_based_on_bits(binary_bits)
    print(label)
    print("-----------------------------------------------------")



def get_label_based_on_bits(binary_bits):
    label = 'VVVTTT'
    version, type_id = binary_bits[:3], binary_bits[3:6]
    version_int, type_id_int = int(version, 2), int(type_id, 2)
    
    is_literal: bool = type_id_int == 4
    
    # literal packet
    if is_literal:
        char = 'A'
        reading = True
        while reading:
            if binary_bits[len(label)] == '0':
                reading = False
            label += char * 5
            char = chr(ord(char) + 1)
            
    # operator packet
    else:
        label += 'I'
        length_type_id = binary_bits[len(label) - 1]
        number__length_type = 15 if length_type_id == '0' else 11
        label += 'L' * number__length_type

        label_subpackets = ''
        reading = True
        char = 'A'

        if number__length_type == 15:
            while reading:
                start = len(label)+len(label_subpackets)
                packet_label = get_label_based_on_bits(binary_bits[start:start+16])
                label_subpackets += char * len(packet_label)
                char = chr(ord(char) + 1)
                if len(label) + len(label_subpackets) + 16 > len(binary_bits):
                    reading = False

            label += label_subpackets
        
        elif number__length_type == 11:
            while reading:
                start = len(label)+len(label_subpackets)
                packet_label = get_label_based_on_bits(binary_bits[start:start+11])
                label_subpackets += char * len(packet_label)
                char = chr(ord(char) + 1)
                if len(label) + len(label_subpackets) + 11 > len(binary_bits):
                    reading = False
                
            label += label_subpackets
            
    return label





def hex_to_binary(hex):
    hex_to_bin_dict = {
        '0': '0000',
        '1': '0010',
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
    part1(data)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()