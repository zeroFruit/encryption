from math import sqrt, floor

def factors(num):
    # data structure to store the factors
    factors = []

    # the same reasoning as we discussed with primality test
    limit = int(floor(sqrt(num)))

    # let's try to find the factors
    # note: if the given number has small factors: we can find it quite fast
    for n in range(2, limit):
        if num %n == 0:
            factors.append([n, num/n])
    
    return factors

if __name__ == "__main__":
    print(factors(210))