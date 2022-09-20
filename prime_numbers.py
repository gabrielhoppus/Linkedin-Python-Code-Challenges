"""Your goal is to write a Python function to find the prime factorization of a given number. It should take an integer value as the input, 
and then return a list containing all of its prime factors. 
For example, calling the function with an input of 630 should return a list containing the values 2, 3, 3, 5, and 7. 
Those are all prime numbers. And if you multiply them together, their product is 630. Calling your function on a prime number, like 13, 
should return a list with just a single value, that prime number."""




def primeFactor(n):
    factor_list = []
    i = 2 #the divisor that will start the factoration
    while (n / i >= 1): #while the result of the factoration is more or equal to 1, continue:
        if (n % i == 0): #if the remainder of the division is equal to zero, add the number to the list and update the dividend
            factor_list.append(i)
            n = n/i
        else: #if the remainder isn't equal to 0, increment to the next item on the list
            i +=1     
    return factor_list #return the list with factors
