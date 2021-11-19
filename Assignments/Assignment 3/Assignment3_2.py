import keyword
import re
dictonary = {}
with open('test1.py') as f: # Cleanup 
    for index, line in enumerate(f): # loop over f, enumerate keeps track of iterations 
        line = re.sub(r'#.*$', '', line) # Remove all comments 
        line = re.sub('"[^"]+"', '', line) # Remove all strings, so no erroes 
        word_list = re.findall(r'[a-zA-ZåäöÅÄÖ]+', line)  # finds all words in, each line. 
        for word in word_list: # for loop in cleaned up world_list, without comments or strings 
            if not keyword.iskeyword(word): # check if keyword 
                if word in dictonary: 
                    x = dictonary.get(word)
                    x.append(index + 1)
                else: 
                    dictonary[word] = [index + 1]
swapped = sorted(dictonary.items(), key = lambda x:len(x[1]), reverse = True)

for i, j in swapped:
    print(i, "", j)

