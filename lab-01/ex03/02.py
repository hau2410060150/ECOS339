def reverse_list(lst):
    return lst[::-1]

input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(',')))

reversed_list = reverse_list(numbers)
print("The reversed list is:", reversed_list)