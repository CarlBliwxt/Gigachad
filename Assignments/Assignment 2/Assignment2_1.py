


def smooth_a(a,n):
    r = []
    temp = [e for e in a]
    #Extendning list with corner elements: 
    for x in range(n): 
        temp.insert(0, temp[0])
        temp.append(temp[-1]) #Negative

    for i in range(0, n):
         r.append(sum(temp[i:i + 2*n + 1])/(2*n+1))
    for i in range(n, len(a) - n): 
        r.append(sum(a[i-n:i+n+1])/(2*n+1))

    print("big" , temp)

    for i in range(len(a) - n, len(a) ): 
         r.append(sum(temp[i-n:i+n+1]) / (2 * n + 1))
    return r



def smooth_b(a,n):

    for i in range(0, n):
         r.append(sum(temp[i-n+n:i + 2*n + 1])/(2*n+1))
    for i in range(n, len(a) - n): 
        r.append(sum(a[i-n:i+n+1])/(2*n+1))
    for i in range(len(a) -n, len(a) ):
         r.append(sum(temp[i-2*n:i  + 1]) / (2 * n + 1))
    return r
x = [1, 2, 6, 4, 5, 0, 1, 2] 
print(x[0])
print('smooth_a(x, 1): ', smooth_a(x, 1)) 
print('smooth_a(x, 2): ', smooth_a(x, 2)) 