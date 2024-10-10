# importing necessary libraries
import string
import random
import re
# HW2
# task1
# function to generate random letters
def generate_random_letters(num):
    res_list = []
    for i in range(num):
        res_list.append(random.choice(string.ascii_letters))
    return res_list
# deciding the number of dict to create through random number
number_of_dicts = random.randint(2, 10)
# creating our list of dictionaries: initially it will be empty ofc
dict_list = []

for i in range(number_of_dicts):
    number_of_letters = 3
    number_of_numbers = 3
    keys_list = generate_random_letters(number_of_letters)
    values_list = random.sample(range(0, 100), number_of_numbers)
    # pairing keys and values from two lists for keys and values
    paired = zip(keys_list, values_list)
    dictionary = dict(paired)
    dict_list.append(dictionary)

print(dict_list)

# task2
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
# calling the function to generate the resulted dictionary
merged_dict = merge_dicts(dict_list)
print(merged_dict)

# HW3
# original string
str = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# counting number of whitespaces for the original string, doing it firstly because the original string will get modified
def count_whitespaces(str):
    count = 0
    for i in str:
        if i == ' ' or i == '\n':
            count += 1
    return count

count_ws = count_whitespaces(str)

# putting new line after dots if there is no new line for splitting and it will help with capitalizing each sentence
def putting_dots_after_new_line(str):
    return re.sub(r"\.(?!\n)", ".\n", str)

str = putting_dots_after_new_line(str)

#cleaning and dividing string into list of values
def convert_string_to_list(str):
    # splitting string by new line so that they will get stored in a list
    lst = str.lower().split('\n')
    # removing unnecessary element from a list after splitting
    while '' in lst:
        lst.remove('')
    return lst

lst = convert_string_to_list(str)

# declaring a list to store last words of each sentence
last_words_lst = []
# for loop to iterate over a list
for i in range(len(lst)):
    # we remove trailing whitespaces for a sentence and capitilize first word of a sentence
    lst[i] = lst[i].strip().capitalize()
    # correcting iz to is
    if lst[i].find(' iz ') != '':
        lst[i] = lst[i].replace(" iz ", " is ")
    # identifying last words of each sentence
    if i >= 1:
        # here storing to a new variable each sentence without a dot so that our last element is a word
        words = lst[i].replace(".", "").split()
        # putting last word to a new list
        if words:
            last_words_lst.append(words[-1])
# joining elements of a list to form a string and putting a dot after, plus capitalizing first word
last_words_str = (" ".join(last_words_lst) + ".").capitalize()
# inserting the sentence with last words to our main list after a sentence specified
lst.insert(4, last_words_str)
# turning our main list of sentences to a string
resulted_string = " ".join(lst)
# printing the results
print(resulted_string)
print("The number of whitespaces: ", count_ws)