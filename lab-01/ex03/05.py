# Function to count the frequency of elements in a list
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Enter a list of words, separated by spaces: ")
word_list = input_string.split()

occurrences = count_occurrences(word_list)
print("The number of occurrences of each element is:", occurrences)