import math
def is_prime(n: int) -> bool:
    next_number_to_check = 2
    while (next_number_to_check <= math.sqrt(n)):
        if (n%next_number_to_check) == 0:
            return(False)
        next_number_to_check = next_number_to_check + 1
    return(True)
#This function works great, as long as the input, N, is an integer.

#type hints
def sum(a:int,b:int) -> int: # these are hints/sudgestions
    return(a+b)

if __name__=="__main__":
    print(is_prime(25.5)) # will give the wrong answer!
    print(sum(1,3))
    print(sum("hello ", "world"))
