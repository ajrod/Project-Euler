from problem3 import Primes

###############################################################################
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

'''
###############################################################################


'''Returns a list of all primes <= n.'''
def genererate_primes(n):
    
    generate_primes = Primes()
    primes = []
    prime = generate_primes.next()
    while (prime <= n):
        primes.append(prime)
        prime = generate_primes.next()
        
    return primes

'''Return a list of prime factors for each number in L. Each numbers individual 
factors are in a nested list.'''
def get_factors(L, primes):
    
    lists = []
    i = len(L) - 1
    while (i > 0):
        number = L[i]
        divisors = []
        for prime in primes:
            while not number % prime:
                divisors.append(prime)
                number = number/prime
        lists.append(divisors)
        i -= 1
        
    return lists


'''Check all the prime factors of each number between 1 and n. 
Return the largest frequency for each factor seen. '''

def determine_max_freq(factor_max_freqs, factor_lists):
    
    for factors in factor_lists:
        for factor in factors:
            count = factors.count(factor)
            if factor not in factor_max_freqs:
                factor_max_freqs[factor] = count     
            elif count > factor_max_freqs[factor]:
                factor_max_freqs[factor] = count


if __name__ == "__main__":
    

    n = 20 #the maximum number as specified by the problem
    
    #the range of numbers from to 1 to n
    numbers = range(1,n+1)
    
    #gets all the possible prime factors for numbers 1 to n
    primes = genererate_primes(n)
    
    #a list of lists for prime factors of each number
    factor_lists = get_factors(numbers, primes)
    
    #this will be used to store the maximum frequency of each prime factor
    factor_max_frequencys = {}
    
    determine_max_freq(factor_max_frequencys, factor_lists)
    
    product = 1
    for factor in factor_max_frequencys:
        product = product * factor**(factor_max_frequencys[factor])
    print product
        
        
        
        
        
        
        
        
        