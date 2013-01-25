import random
import math
###############################################################################
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
###############################################################################

'''An iterator for a series of primes.'''
class Prime(object):
    
    def __init__(self):
        self.prime = 2
        self.primes = [2,3] #a list of all primes created by the iterator
    '''Return true iff there is more in the series.'''
    def has_next(self):
            return true #infinite number of primes
    '''Get the prime in the series and set up the next.'''
    def next(self):
        old_prime = self.prime
        self.set_next()
        return old_prime
    '''Set the next prime in the series.'''
    def set_next(self):
        
        #Two is the only even prime. This must be hard coded
        #since i increment by two below assuming that previous prime
        #was odd.
        if self.prime == 2: 
            self.prime = 3
        else:
            #previous prime must be odd, add two to check the next odd number
            new_prime = self.prime + 2
            ct = 0 
            p = 0
            #The next prime is set by checking the next odd number
            #and testing if that new number can be factored by any
            #of the previous primes created by the iterator. Using a list of
            #previous primes allows us to skip all composite numbers.
            #The number being tested only needs to be checked by primes
            #that are smaller then the root of the number since a factor
            #cannot be larger than the root.
            while (ct < len(self.primes) and p <= new_prime**(1/2.0)):
                p = self.primes[ct]
                #check if the current number can be factored by a previous prime
                if not new_prime%p:
                    new_prime += 2 #check next odd number
                else:
                    ct+=1
            self.primes.append(new_prime)
            self.prime = new_prime
if __name__ == "__main__":
    
    prime_iterator = Prime()
    number = 600851475143 #the number from the problem
    prime = prime_iterator.next()
    largest_factor = prime
    while (prime <= number):
        
        #while the number is divisible by the prime divide out the factor 
        #since a number may have the same factor many times
        while number%prime == 0: 
            #primes are always increasing so next factor seen is larger
            #then previous factor
            largest_factor = prime 
            number = number/prime #divides out the factor
        #get next potential factor
        prime = prime_iterator.next()
        
    print "Largest factor", largest_factor
    