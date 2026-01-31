def create_tuple_from_list(lst):
    return tuple(lst)

input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = create_tuple_from_list(numbers)
print("List:", numbers)
print("Tuple from list:", my_tuple)