#Author: Alexander Rodrigues

import math

###############################################################################
'''
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Question made by http://projecteuler.net/.
'''
###############################################################################

'''Calculate the arithmetic sum given a divisor and an exclusive upper bound
on the series.
I.e if divisor is d return (1)d + (2)d + (3)d + ... + (flr((bound - 1)/d))d.'''
def arith_sum(divisor):
    k = math.floor((uBound - 1)/divisor) 
    return (int)(divisor*(k + 1) * k)/2

if __name__ == "__main__":
    
    global uBound
    uBound = 1000 #the upper bound designated by the problem
    
    #Niave solution; trial divisor test
    #Runs in O(bound)
    num = 0   #counter for which number we are checking
    accum = 0 #accumulator for the sum of all multiples
    while (num < uBound):
        #check if the current num is divisble by either 3 or 5
        if num % 3 == 0 or num % 5 == 0:
            accum += num
        num += 1
    print "Trial by division:", accum
    
    #Better solution using arithmetic sums
    #Runs in constant time
    print "Arithmetic sums:", arith_sum(3) + arith_sum(5) - arith_sum(15)
    
    