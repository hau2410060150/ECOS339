def delete_element(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'

result = delete_element(my_dict, key_to_delete)

if result:
    print("The element has been deleted from the dictionary:", my_dict)
else:
    print("The key to be deleted was not found in the dictionary.")