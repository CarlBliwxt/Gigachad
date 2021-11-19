# Assignment 3, excercise 1 

import re 

n = int(input("How many common words?: ")) # User input 
frequency = {}

with open("test.txt","r") as document: # Clean up everything that is essential 
    text = document.read() # reads the document line by line
    document.close() 
    text = text.lower()  # Turns every char to a lower, so Carl and carl is not two different words
    word_string = text.split() # Splits into each word in a list 
    unique_words = set(word_string) # Stores duplicates in the same value,  

for word in word_string: # For loop in the entire string 
    count = frequency.get(word, 0) 
    frequency[word] = 1 + count
frequency_list = list(frequency.items()) # creates a list


swapped = sorted(frequency_list, key = lambda x:(x[1]), reverse = True)
print("The total number of words", len(word_string))
for x in range(0, n): 
    print(f"{swapped[x][0]}, {swapped[x][1]}")


