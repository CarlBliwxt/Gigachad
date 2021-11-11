# Assignment 1

import re 

n = int(input("How many common words?: "))

document = open("test.txt", "r")
text = document.read()
document.close()
text = text.lower()
#print(text)
word_string = text.split()
unique_words = set(word_string)
#print(unique_words)

frequency = {}
for word in word_string:
    count = frequency.get(word,0) 
    frequency[word] = count +1
frequency_list = list(frequency.items())
#print(frequency_list[1])

swapped = sorted(frequency_list, key =lambda x:(x[1]), reverse = True)
print(swapped)

for x in range(0,n): 
    print(f"{swapped[x][0]}, {swapped[x][1]}")
print(len(word_string))

