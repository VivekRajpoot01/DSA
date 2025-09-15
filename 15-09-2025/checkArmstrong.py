# Check Armstrong number

def check_armstrong(n):
    num = n
    res = 0
    while(num>0):
        digit = num %10
        res = res + (digit**3)
        num = num//10
        
    return n==res

n = int(input())
print(check_armstrong(n))
