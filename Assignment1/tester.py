#import assignment1

'''for i in range(100):
    print(str(i)+"\t"+str(assignment1.is_prime(i)))
print(str(assignment1.is_prime(4)))'''
# print(assignment1.are_relatively_prime(3,9))
# print(assignment1.are_relatively_prime(2,9))
#print(assignment1.primes(100))
#print(assignment1.is_prime(5))
#print(assignment1.is_prime(5))
def prime_decomposition(number):
decomposition = []
done = False
x = 1
while (not done):
    x = decompose(number//x)
    if x>0:
        decomposition.append(x)
        else:
        done = True
        return decomposition
    
def decompose(number):
	# find the smallest divisor and return it
	for i in range(2, number + 1):
		if (number % i == 0):
			# found the divisor
			return i
	return 0

def prime_decomposition(number):
	decomposition = []
	done = False
	x = 1
	while (done == False):
		x = decompose(number//x)
        if (x > 0):
            decomposition.append(x)
            else:
                done = True
                return decomposition
    
xtion(2))
