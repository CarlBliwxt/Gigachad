import keyword
import re
dictonary = {}
with open('test1.py') as f:
    for index, line in enumerate(f):
        line = re.sub(r'#.*$', '', line)
        line = re.sub('"[^"]+"', '', line)
        word_list = re.findall(r'[a-zA-ZåäöÅÄÖ]+', line)    
        for word in word_list:
            if not keyword.iskeyword(word):
                if word in dictonary: 
                    x = dictonary.get(word)
                    x.append(index+1)
                else: 
                    dictonary[word] = [index+1]

swapped = sorted(dictonary.items(), key = lambda x:len(x[1]), reverse = True)

for i, j in swapped:
    print(i, "", j)
    
    
#print(dictonary)
        #print("{}: {}".format(index, line.split()))
