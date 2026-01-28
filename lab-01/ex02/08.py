def is_divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    
    if decimal_number % 5 == 0:
        return True
    else:
        return False


binary_string = input("Enter binary numbers (separated by commas): ")

binary_list = binary_string.split(',')
divisible_by_5 = [b for b in binary_list if is_divisible_by_5(b)]

if len(divisible_by_5) > 0:
    result = ','.join(divisible_by_5)
    print("Binary numbers divisible by 5 are:", result)
else:
    print("There are no binary numbers divisible by 5 in the given input.")