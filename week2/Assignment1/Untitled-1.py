
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
    print 'foo'
    