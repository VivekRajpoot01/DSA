# Check palindrome

def check_palindrome(n):
    num = n
    res = 0
    while num>0:
        digit = num %10
        res = res*10 + digit
        num = num//10
    
    return n==res


n = int(input())
print(check_palindrome(n))
    
