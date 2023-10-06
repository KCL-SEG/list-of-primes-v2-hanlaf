"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    lastPrime = 1
    
    if (number_of_primes <= 0):
        raise ValueError

    for i in range(number_of_primes):
        if number_of_primes > 1:
            # Work out the prime
            currentPrime = lastPrime
            foundPrime = False
            while not foundPrime:
                currentPrime += 1
                if (check_prime(currentPrime) == True):
                    foundPrime = True
                    list.append(currentPrime)
                    lastPrime = currentPrime
        elif number_of_primes == 1:
            list.append(2)
            break
    return list

def check_prime(currentPrime):
    for i in range (2, currentPrime):
        if (currentPrime % i == 0) and i != currentPrime:
            return False
    return True