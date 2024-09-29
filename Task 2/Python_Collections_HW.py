import string
import random
#task1
#function to generate random letters
def generate_random_letters(num):
    res_list = []
    for i in range(num):
        res_list.append(random.choice(string.ascii_letters))
    return res_list
#deciding the number of dict to create through random number
number_of_dicts = random.randint(2, 10)
#creating our list of dictionaries: initially it will be empty ofc
dict_list = []

for i in range(number_of_dicts):
    number_of_letters = 3
    number_of_numbers = 3
    keys_list = generate_random_letters(number_of_letters)
    values_list = random.sample(range(0, 100), number_of_numbers)
    #pairing keys and values from two lists for keys and values
    paired = zip(keys_list, values_list)
    dictionary = dict(paired)
    dict_list.append(dictionary)

print(dict_list)

#task2
def merge_dicts(dicts):
    result = {}

    # Iterate over each dictionary and each key-value pair within
    for idx, d in enumerate(dicts, start=1):
        for key, value in d.items():
            # If the key is new or found with a larger value, update the result
            if key in result and value > result[key]:
                new_key = f"{key}_{idx}"  # Rename key with dict number
                result.update({new_key: value})
                result.pop(key)
            else:
                result.update({key: value})

    return result
#calling the function to generate the resulted dictionary
merged_dict = merge_dicts(dict_list)
print(merged_dict)

