


def is_prime(number):
    # number is int and > 1    
    for i in range(2, number//2 + 1):
            # from 2...to...half of number
            
            # if number mod i (divide by i and return remainder) is equal to zero, is_factor true. 
            is_factor = number % i == 0 
            if is_factor:
                # number ain't prime
                return False
    # got through for loop prime checker without returning false, so 
    return True

def are_relatively_prime(num1, num2):
    numbers = (num1, num2)
    # num1 and num2 are > 1, ints
    # factors contains 2 rows (first for num1, second for num2) and as many columns as factors for both numbers 
    factors = [] # does not include 1!!
    factors.append([]) # for num1
    factors.append([]) # for num2
    for number_index in range(2):
        for possible_factor in range(2, numbers[number_index] + 1):
            is_factor = numbers[number_index] % possible_factor == 0
            if is_factor:
                # found a factor, now add it to factors list
                factors[number_index].append(possible_factor)
    # now the list factors should contain all factors of each number. 
    # check if any of the factors match
    for factor_to_check in factors[0]:
        for other_factor in factors[1]:
            if factor_to_check == other_factor:
                # numbers have a common factor, so they are not relatively prime
                return False
    # checked all factors and did not return, so numbers must be common factors
    return True

def primes(number):
    primes_under_number = []
    for i in range(1, number + 1):
        if is_prime(i):
            primes_under_number.append(i)
    return primes_under_number

def decompose(number, results):
        for i in range(2, number +1):
            if number % i == 0:
                # divisible by i, we found a factor, now look for the next one
                results.append(i)
                return decompose(number//i, results)

def prime_decomposition(number):
    results = []
    decompose(number, results)
    return results

if __name__ =="__main__":
    print(prime_decomposition(100))
