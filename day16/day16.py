with open('input.txt') as f:
    data = [
        f.read().rstrip(),               # Live 0
        
        # Part 1 test cases:
        'D2FE28',                         # Test 1
        '38006F45291200',                 # Test 2
        'EE00D40C823060',                 # Test 3
        '8A004A801A8002F478',             # Test 4 -> version sum 16
        '620080001611562C8802118E34',     # Test 5 -> version sum 12
        'C0015000016115A2E0802F182340',   # Test 6 -> version sum 23
        'A0016C880162017C3686B18A3D4780', # Test 7 -> version sum 31
        
        # Part 2 test cases:
        'C200B40A82',                     # Test 8  -> value 3
        '04005AC33890',                   # Test 9  -> value 54
        '880086C3E88112',                 # Test 10 -> value 7
        'CE00C43D881120',                 # Test 11 -> value 9
        'D8005AC2A8F0',                   # Test 12 -> value 1
        'F600BC2D8F',                     # Test 13 -> value 0
        '9C005AC2F8F0',                   # Test 14 -> value 0
        '9C0141080250320F1802104A08'      # Test 15 -> value 1
    ]

TYPE_ID_LITERAL      = 4
TYPE_ID_SUM          = 0
TYPE_ID_PRODUCT      = 1
TYPE_ID_MIN          = 2
TYPE_ID_MAX          = 3
TYPE_ID_GREATER_THAN = 5
TYPE_ID_LESS_THAN    = 6
TYPE_ID_EQUAL_TO     = 7

LENGTH_TYPE_ID_TOTAL_LENGTH         = 0
LENGTH_TYPE_ID_NUMBER_OF_SUBPACKETS = 1

def operate(type_id, packets):
    values = [packet['value'] for packet in packets]
    if type_id == TYPE_ID_SUM:
        return sum(values)
    elif type_id == TYPE_ID_PRODUCT:
        prod = 1
        for value in values:
            prod *= value
        return prod
    elif type_id == TYPE_ID_MIN:
        return min(values)
    elif type_id == TYPE_ID_MAX:
        return max(values)
    elif type_id == TYPE_ID_GREATER_THAN:
        assert(len(values) == 2)
        return int(values[0] > values[1])
    elif type_id == TYPE_ID_LESS_THAN:
        assert(len(values) == 2)
        return int(values[0] < values[1])
    elif type_id == TYPE_ID_EQUAL_TO:
        assert(len(values) == 2)
        return int(values[0] == values[1])
    else:
        raise Exception('Unknown packet type:', type_id)
    return 0

def parse_header(string):
    return {
        'version':    int(string[:3], 2),
        'type_id':    int(string[3:6], 2),
        'parsed_len': 6
    }

def parse_literal(string):
        data = string
        was_not_last = True
        literal = ''
        parsed_len = 0
        while was_not_last:
            was_not_last = data[0] == '1'
            literal += data[1:5]
            data = data[5:]
            parsed_len += 5
        return int(literal, 2), parsed_len

def parse_operator(string):
    operator = {
       'length_type': int(string[0])
    }
    version_sum = 0
    if operator['length_type'] == LENGTH_TYPE_ID_TOTAL_LENGTH:
        operator['total_length'] = int(string[1:16], 2)
        sp_string = string[16 : 16 + operator['total_length']]
        operator['subpackets_string'] = sp_string
        operator['subpackets'] = []
        while sp_string:
            subpacket, sp_string = parse_packet(sp_string)
            operator['subpackets'].append(subpacket)
            version_sum += subpacket['version_sum'] if 'version_sum' in subpacket else subpacket['version']
        parsed_len = 16 + operator['total_length']
    elif operator['length_type'] == LENGTH_TYPE_ID_NUMBER_OF_SUBPACKETS:
        operator['number_of_subpackets'] = int(string[1:12], 2)
        parsed_len = 12
        sp_string = string[12:]
        operator['subpackets_string'] = sp_string
        operator['subpackets'] = []
        for i in range(operator['number_of_subpackets']):
            assert(sp_string != '')
            subpacket, sp_string = parse_packet(sp_string)
            operator['subpackets'].append(subpacket)
            parsed_len += subpacket['parsed_len']
            version_sum += subpacket['version_sum'] if 'version_sum' in subpacket else subpacket['version']
    else:
        raise Exception('Unknown length type:', operator['length_type'])
    return operator, parsed_len, version_sum

def parse_packet(string):
    packet = parse_header(string)
    if packet['type_id'] == TYPE_ID_LITERAL:
        packet['value'], plen = parse_literal(string[6:])
        packet['l_string'] = string[6:]
    else:
        packet['operator'], plen, version_sum = parse_operator(string[6:])
        packet['version_sum'] = packet['version'] + version_sum
        packet['value']       = operate(packet['type_id'], packet['operator']['subpackets'])
    packet['parsed_len'] += plen
    return packet, string[packet['parsed_len']:]

string = ''.join([str(bin(int(c, 16)))[2:].zfill(4) for c in data[0]])
packet, remaining_string = parse_packet(string)

print('Part 1:', packet['version_sum'])
print('Part 2:', packet['value'])
