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
    binary_bits = hex_to_binary('620080001611562C8802118E34')
    #binary_bits = '11101110000000001101010000001100100000100011000001100000'
    #print(binary_bits)
    
    label = get_label_based_on_bits(binary_bits)
    print(binary_bits)
    print(label)
    

    #print("-----------------------------------------------------")

    



def get_label_based_on_bits(binary_bits):
    
    label = 'VVVTTT'
    version, type_id = binary_bits[:3], binary_bits[3:6]
    version_int, type_id_int = int(version, 2), int(type_id, 2)
    #print(binary_bits)
    print(version_int)
   
    is_literal: bool = type_id_int == 4
    
    # literal packet
    if is_literal:
        label += label_literal_packet(label, binary_bits)
            
    # operator packet
    else:
        label += 'I'
        length_type_id = binary_bits[len(label) - 1]
        number__length_type = 15 if length_type_id == '0' else 11
        label += 'L' * number__length_type

        label_subpackets = ''
        reading = True
        char = 'A'
        #print(number__length_type)

        if number__length_type == 15:
            while reading:
                start = len(label)+len(label_subpackets)

                
                binary_number_of_packets = binary_bits[7:22]
                number_of_packets = int(binary_number_of_packets, 2)
                #print("total length of subpackets", number_of_packets)

                label_subpacket = get_label_based_on_bits(binary_bits[start:])
                #print(label_subpacket)
                label_subpackets += char * len(label_subpacket)

                

                char = chr(ord(char) + 1)
                if len(label) + len(label_subpackets) + 11 > len(binary_bits):
                    reading = False
                
                
                
                
            
        
        elif number__length_type == 11:
            binary_number_of_packets = binary_bits[7:18]
            number_of_packets = int(binary_number_of_packets, 2)
            reading = True

            while reading:               
                start = len(label)+len(label_subpackets)
                
                packet_label = get_label_based_on_bits(binary_bits[start:])
                #print(packet_label)
                label_subpackets += char * len(packet_label)
                char = chr(ord(char) + 1)
                if len(label) + len(label_subpackets) + 11 > len(binary_bits):
                    reading = False
                
        label += label_subpackets
    #print(label)
    return label



def label_literal_packet(label, binary_bits):
    new_label = ''
    char = 'A'
    reading = True
    while reading:
        if binary_bits[len(label)+len(new_label)] == '0':
            reading = False
        new_label += char * 5
        char = chr(ord(char) + 1)
    return new_label
    



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
    part1(data)

    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()