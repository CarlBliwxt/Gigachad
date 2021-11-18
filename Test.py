import math 


print(-5 // 2 )
print(-(5//2))
print(37%10) # Hur många gånger någonting får plats, det som blir kvar är det som printas
print(10.**2)


def celcius_to_fahrenheit(c):
    return 9/5 * c + 32 

def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    return c

print(fahrenheit_to_celsius(77))
print(celcius_to_fahrenheit(25.0))

def howmany(sum):
    s = 0
    n = 0
    while n < sum: 
         n += 1
         s += 1/n
    return n


def digits(x):


