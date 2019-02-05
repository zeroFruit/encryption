from math import sqrt, floor

def is_prime(num):

    # numbers smaller than 2 cannot be primes
    if num <= 2: return False
    
    # even numbers cannot be primes
    if num%2==0: return False
    
    # we have already checked numbers < 3
    # finding primes up to N we just have to check numbers up to sqrt(N)
    # increment by 2 because we have already consdiered even numbers
    for i in range(3, int(floor(sqrt(num))), 2):
        if num%i == 0:
            return False
    
    return True

if __name__ == "__main__":
    print(is_prime(99194853094755497))
    