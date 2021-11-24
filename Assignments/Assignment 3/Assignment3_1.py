# Assignment 3, excercise 1 

import re 

n = int(input("How many common words?: ")) # User input 
frequency = {}

with open("test.txt", encoding ='utf8') as document: # Using unicoe instead to handle swedish characters
    text = document.read() # reads the document line by line
    text = text.lower()# Turns every char to a lower, so Carl and carl is not two different words
    word_list = re.findall((r'[a-åäö]+'), text)
    unique_words = set(word_list) # Stores duplicates in the same value, so we only get unique words 

print("Amount of unique words ", len(unique_words))

for word in word_list: # For loop in the entire string 
    count = frequency.get(word, 0) 
    frequency[word] = 1 + count
frequency_list = list(frequency.items()) # creates a list


swapped = sorted(frequency_list, key = lambda x:(x[1]), reverse = True) # Sorts so it is descending order 
print("The total number of words", len(word_list))
for x in range(0, n): 
    print(f"{swapped[x][0]}, {swapped[x][1]}")


