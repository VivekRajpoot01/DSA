# To count the number of digit in a number
n = 5873
num = n # creating new var so that it does not affect input variable 
count = 0
while num>0:
    digit = num%10
    count +=1
    num = num//10
    
print(count)
# Here time complexity would be O(log10(n)) as we are dividing constantly with 10

# we can also do this code as
res = int(log10(n)+1)
print(res)
