# Print Factors of a number

#first we will find the factors using brute force method in this we try to check from 1 to n whether it is factor or not  
n = 10
for i in range(1,n+1):
    if n %i ==0:
        print(i)
#here time complexity would be O(n)        

# if we go for better solution than this then what will find we only need to find the factor between 1 to n//2  and number itself is also divisible
for i in range(1,n//2):
    if n%i ==0:
        print(i)
    print(n)    
        
# here time complexity would reduced to O(n/2), but we approximately take as O(n) but in actual number if operations reduced

# we also have an optimal solution for that time complexity would be O(sqrt(n))

from math import sqrt
llst = []
for i in range(1,int(sqrt(n)+1)):
    if n%i==0:
        llst.append(i)
        if(n//i!=i):
            llst.append(n//i)
