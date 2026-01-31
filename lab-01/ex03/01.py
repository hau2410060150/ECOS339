def sum_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total


input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(',')))

even_sum = sum_even_numbers(numbers)
print("The sum of even numbers in the list is:", even_sum)