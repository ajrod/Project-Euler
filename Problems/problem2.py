#Author: Alex Rodrigues

###############################################################################
'''
Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
'''
###############################################################################

if __name__ == "__main__":
    
    uBound = 4 * 10**6 #upper bound as designated by the problem
    
    #base cases for the Fibonnaci sequence
    fib1 = 1 
    fib2 = 2
    accum = 0 #accumulator for the sum
    while (fib2 < uBound):
        
        #add the fibonacci number if it is even
        if (fib2 % 2 == 0):
            accum += fib2
        
        #move the fibonacci numbers forward in the series
        fib1, fib2 = fib2, fib1 + fib2
    print "Total sum", accum