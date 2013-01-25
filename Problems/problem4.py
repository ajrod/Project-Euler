#author: Alexander Rodrigues

'''
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Question made by http://projecteuler.net/.
'''

'''Return true iff n is a palindrome.'''
def is_palimdrone(n):
    
    return str(n) == str(n)[-1::-1]


if __name__ =="__main__":
    
    f1 = 999  #start with largest 3-digits
    largestPal = 0
    #Brute force approach; try all possible combinations of 3digit products.
    #That is try 999x[100-999], 998x[100-999], ..., 100x[100-999].
    while (f1 >= 100):
        f2 = 999
        while (f2 >= 100):
            tmp = f1*f2
            if is_palimdrone(tmp) and largestPal < tmp:
                largestPal = tmp
            f2 -= 1
        f1 -= 1
    print "Largest palindrome made from 2 3digit numbers", largestPal