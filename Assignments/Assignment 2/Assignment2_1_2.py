# Program 
def smooth_a(a,n): # Original solution the one presented at the lesson
    r = []
    #Corner elements
    temp = a.copy() # Creating a new list by copying a into it
    for x in range(n): # I had accidentaly changed this to 0 len(a) -1, corrected
        temp.insert(x, a[0]) # Insert the first element of a at spot 0
        temp.append(a[-1]) # Insert the last element, negative index makes end point.
    for i in range(n, len(temp) - n):
        interval = temp[(i-n):i + (n+1)]
        sumof_a = sum(interval) # From i-n to i+n+1, from looking at excericse D
        amount_a = 2*n + 1 
        r.append(sumof_a/amount_a) # Appends to new r.
    return r

def smooth_a1(a,n): # Not sure why this work, with pytest but it does work, this was my original solution until i read that you should not use if 
    r = []
    for i in range(0, len(a)):
        temporary_outside_right = (i + n) - (len(a)-1) # how many points outside the given interval, -1 because python starts at 0 
        temporary_outside_left = (i-n) * -1 # same here but the left side of the interval 
        if  (i - n) < 0:  # We check if it is in the interval, 
            interval = a[0:i + (n+1)] 
            sum_of_a = sum(interval)
            temp = a[0] * temporary_outside_left #
            amount_a = (2*n +1)
            r.append((sum_of_a + temp)/amount_a)
        elif (i + n > len(a) - 1 ):  # Basically same as smooth_b,
            interval = a[(i-n):len(a)]
            sum_of_a = sum(interval)
            temp = a[-1] * temporary_outside_right
            amount_a = (2*n +1)
            r.append((sum_of_a + temp)/amount_a) 
        elif (i - n < 0 and i + n > len(a) -1): 
            interval = a[0:len(a)]
            sum_of_a = sum(interval)
            temp = a[-1] * temporary_outside_right + a[0] * temporary_outside_left
            amount_a = (2*n +1)
            r.append((sum_of_a + temp)/amount_a)    
        else: 
            interval = a[(i - n): i + (n+1)]
            sum_of_a = sum(interval)
            amount_a = (2*n +1)
            r.append((sum_of_a/amount_a))
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
    for i in range(len(b) - n, len(b)): 
        interval = b[(i-n): len(b)]
        sumof_b = sum(interval)
        length = len(interval)
        r.append(sumof_b/length)
    return r

def round_list(a_list, ndigits):
    rounded_list = [round(x, ndigits) for x in a_list]
    return rounded_list


x = [1, 2, 6, 4, 5, 0, 1, 2] 
print('smooth_a(x, 1): ', smooth_a(x, 1)) 
print('smooth_a(x, 2): ', smooth_a(x, 2)) 
print('smooth_b(x, 1): ', smooth_b(x, 1)) 
print('smooth_b(x, 2): ', smooth_b(x, 2))
print('smoooth_a(x,10', smooth_a(x, 10))
print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))