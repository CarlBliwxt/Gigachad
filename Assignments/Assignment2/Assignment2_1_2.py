
def smooth_a(a,n):
    r = []
    #Corner elements
    temp = a.copy() # Creating a new list by copying a into it
    for x in range(n): 
        temp.insert(0, a[0]) # Insert the first element of a at spot 0
        temp.append(a[-1]) # Insert the last element, negative index starts at the end
    for i in range(n, len(temp) -n ):
        interval = temp[(i-n):i + (n+1)]
        sumof_a = sum(interval) # From i-n to i+n+1, from looking at excericse D
        amount_a = 2*n + 1 
        r.append(sumof_a/amount_a) # Appends to new r.
    return r


def smooth_b(b,n):
    r =[]
    # We split it into three intervals, the middle one stays the same
    for i in range(0, n): #Suppose to go from 0 to n,
        #We want to start at the first element
        # And take n+1 steps right 
        interval = b[0:i + (n+1)]
        sumof_b = sum(interval)
        # We then need to long we have "traveled"
        length = len(interval)
        r.append(sumof_b/length)
    # In this interval, we define the range so that, it has to compute without touching the edges
    for i in range(n, len(b) - n): 
        interval = b[i-n:i+(n+1)] # interval 
        sumof_b = sum(interval) #sum
        amount_b = (2*n+1) # length
        r.append(sumof_b/amount_b)
    
    # Here i starts at len(a) - n, so to get on the left side, we do i-n,
    # To get it on the right side it needs to go the full length of a and needs to stop there
    for i in range(len(b) - n, len(b) ): 
        interval = b[(i-n): len(b)]
        sumof_b = sum(interval)
        length = len(interval)
        r.append(sumof_b/length)
    return r

def round_list(a_list, ndigits):
    rounded_list = [round(x, ndigits) for x in a_list]
    return rounded_list


x = [1, 2, 6, 4, 5, 0, 1, 2] 
print(x[0:1])
print('smooth_a(x, 1): ', smooth_a(x, 1)) 
print('smooth_a(x, 2): ', smooth_a(x, 2)) 
print('smooth_b(x, 1): ', smooth_b(x, 1)) 
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smoooth_a(x,10', smooth_a(x, 10))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))