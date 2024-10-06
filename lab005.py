#Part 1
def is_valid_part(part):
    if part.isdigit() and 0 <= int(part) <= 255 and not (len(part) > 1 and part[0] == '0'):
        return True
    else:
        return False

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True

print(is_valid_part('255'))  # True
print(is_valid_part('256'))  # False
print(is_valid_part('01'))  # False
print(is_valid_part('0'))  # True

print(is_valid_ip("192.168.1.1"))  #true
print(is_valid_ip("192.168.256.1"))  #false
print(is_valid_ip("192.168.1"))  #false
print(is_valid_ip("192.168.01.1"))  #false

# Part 2
def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(10)) #'1010'
print(decimal_to_binary(255))  #'11111111'
print(decimal_to_binary(1))  #'1'

def binary_to_decimal(b):
    exp = len(b)-1
    if exp < 0:
        return 0
    return int(b[0])*(2**exp)+binary_to_decimal(b[1:])

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 10

#Part 3
def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return ValueError("Invalid IP address")
    parts = ip.split('.')
    binary_parts = []
    for part in parts:
        binary_parts.append(decimal_to_binary(int(part)))
    binary_ip = ''
    for i in range(len(binary_parts)):
        binary_ip += binary_parts[i]
        if i < len(binary_parts) - 1:
            binary_ip += '.'
    return binary_ip

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"