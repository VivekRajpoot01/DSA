# we have to find the fibonacci number using recursion

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    
# Here time complexity would be O(2^n) as we are doing two operations every time
# and space complexity would also be same O(2^n) 
