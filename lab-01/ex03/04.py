def access_tuple_elements(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element


input_tuple = eval(input("Enter a tuple, for example (1, 2, 3): "))

first, last = access_tuple_elements(input_tuple)

print("First element:", first)
print("Last element:", last)