# recursion is the best
# recutsion must have base cases?
def factorial(n):
    if (n==0):
        # base case
        return 1
    else:
        return(n*factorial(n-1))
    
def fibonacci(n):
    if (n==1):
        return (0)
    if (n==2):
        return(1)
    else:
        return ( fibonacci(n-1)+fibonacci(n-2))
    return
if __name__=="__main__":
    print(factorial(3))
    print(fibonacci(7))
    
    