import re
from collections import Counter
import csv

# Open the text file
with open('feeds.txt', 'r') as file:
    # Read the content of the file
    text = file.read()

    # Convert all text to lowercase
    text = text.lower()

    # Use regex to find words, which allows for more accurate counting by filtering out punctuation
    words = re.findall(r'\w+', text)

    # Use Counter to get occurrences of each word
    word_count = Counter(words)

# Define the path to the output CSV file
csv_file_path = 'word_counts.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(['Word', 'Count'])

    # Write the word counts
    for word, count in word_count.items():
        csvwriter.writerow([word, count])

print(f'Word counts have been saved to {csv_file_path}')

# Define the path to the output CSV file
csv_file_path = 'word_counts_detailed.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(['Word', 'Count_all', 'Count_uppercase', 'Percentage'])

    # Total number of words in the document to calculate percentages
    total_words = sum(word_count.values())

    # Write the word counts and details
    for word, count in word_count.items():
        count_uppercase = sum(1 for char in word if char.isupper())
        percentage = (count / total_words) * 100
        csvwriter.writerow([word, count, count_uppercase, f"{percentage:.2f}%"])

print(f'Detailed word counts and statistics have been saved to {csv_file_path}')