"""Your goal is to write a Python function to find the prime factorization of a given number. It should take an integer value as the input, 
and then return a list containing all of its prime factors. 
For example, calling the function with an input of 630 should return a list containing the values 2, 3, 3, 5, and 7. 
Those are all prime numbers. And if you multiply them together, their product is 630. Calling your function on a prime number, like 13, 
should return a list with just a single value, that prime number."""


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
factor_list = []

def primeFactor(n):
    i = 0 #the position in the primes list 0 = 2, 1 = 3 and so on
    while (n / primes[i] >= 1): #while the result of the factoration is less or equal to 1, continue:
        if (n % primes[i] == 0): #if the remainder of the division is equal to zero, add the number to the list and update the dividend
            factor_list.append(primes[i])
            n = n/primes[i]
        else: #if the remainder isn't equal to 0, increment to the next item on the list
            i +=1     
    return factor_list #return the list with factors
