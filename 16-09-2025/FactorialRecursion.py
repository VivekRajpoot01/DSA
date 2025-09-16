# finding factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
# Here time complexity would be O(n)
# and space complexity would also be O(n) as it is using stack space
