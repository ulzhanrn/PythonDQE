# importing necessary libraries
import re
# original string
str = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# counting number of whitespaces for the original string, doing it firstly because the original string will get modified
count = 0
for i in str:
    if i == ' ' or i == '\n':
        count += 1

# putting new line after dots if there is no new line for splitting and it will help with capitalizing each sentence
str = re.sub(r"\.(?!\n)", ".\n", str)

# splitting string by new line so that they will get stored in a list
lst = str.lower().split('\n')
# removing unnecessary element from a list after splitting
while '' in lst:
    lst.remove('')
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
print("The number of whitespaces: ", count)