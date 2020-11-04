import math

def isPrimeNumber( n ):
    
    # Returns True if n is prime number else False

    # Make sure n is a positive integer
    # if not then make it positive intger
    n = abs(int(n))

    # ----- some simple and fast tests ---------
    
    # The number n is less 2 i-e 0 or 1
    if n < 2: return False
    
    # The number n is 2
    if n == 2: return True

    # The number n is even then not prime
    if n % 2 == 0: return False

    # Check odd numbers less than the square root of the given number n for possible factors 
    r = math.sqrt( n )
    
    # start from 3, we have already test for 0, 1 and 2
    x = 3 
    while x <= r:
        if n % x == 0: return False  # A factor was found, so number is not prime
        x += 2 # Increment to the next odd number

    # No factors found, so number is prime  
    return True 

lista_tal = []
for i in range(1,101):
    lista_tal.append(i)
    if i%10 == 0:
        print(i)
    if isPrimeNumber(i):
        print(i)