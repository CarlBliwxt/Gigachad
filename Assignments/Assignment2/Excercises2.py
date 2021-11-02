

def nonnegative(m):
    m = [-1, 1, 2, 3, 0]
    n = []
    for x in m: 
        if x >= 0: 
            n.append(x)
    print (n)

def between(a_list, low, high ):
    n_list = []
    for x in a_list: 
        if ( low < x < high):
            n_list.append(x)
    return n_list

def smooth(a):
    new =[]
    new.append(a[0])
    for i in range(1, len(a)- 1):
        new.append(sum(a[i-1:i+2])/3)



l = [3, 1, 8, 19, 2, 5, 12]
print(between(l, 3, 12)) 
m = [-1, 1, 2, 3, 0]
nonnegative(m)