# Program 
def smooth_a(a,n):
    r = []
    #Corner elements
    temp = a.copy() # Creating a new list by copying a into it
    for i in range(0, len(a)):
        temp_outside_high = (i + n) - len(a) -1 
        temp_outside_low= ((i-n) * -1)
    for x in range(0, len(a)): 
        temp.insert(x, a[0]) # Insert the first element of a at spot 0
        temp.append(a[-1]) # Insert the last element, negative index makes end point. 
    for i in range(n, len(temp) - n):
        interval = temp[(i-n):i + (n+1)]
        sumof_a = sum(interval) # From i-n to i+n+1, from looking at excericse D
        amount_a = 2*n + 1 
        r.append(sumof_a/amount_a) # Appends to new r.
    return r


def smooth_b(lista, n):
    res = []

    for i in range(0, len(lista)):
        temp_high = (i + n) - (len(lista) - 1)
        temp_low = ((i - n) * -1)
        if i-n < 0 and i+n > len(lista) - 1:
            amount = temp_low + temp_high
            res.append((sum(lista[0:len(lista)]))/(2*n+1-amount))
        elif i-n < 0:
            res.append((sum(lista[0:i+n+1]))/(2*n+1-temp_low))
        elif i + n > len(lista) - 1:
            res.append((sum(lista[i - n:len(lista)]) ) / (2 * n + 1- temp_high))
        else:
            res.append(sum(lista[i - n:i + n + 1]) / (2 * n + 1))
    return res


def round_list(calc_list, n):
    return [round(z, n) for z in calc_list]


x = [1, 2, 6, 4, 5, 0, 1, 2] 
print(len(x))
print(x[0:1])
print('smooth_a(x, 1): ', smooth_a(x, 1)) 
print('smooth_a(x, 2): ', smooth_a(x, 2)) 
print('smooth_b(x, 1): ', smooth_b(x, 1)) 
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smoooth_a(x,10', smooth_a(x, 10))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))