
def smooth(a,n):
    r = []
    #Nested loop
    for i in range(0, len(a)):
        tempfirst = sum(a[i-n])