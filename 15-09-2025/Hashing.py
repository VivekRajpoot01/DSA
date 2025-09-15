# Hashing
# In hashing we first we solve any problem and store the data into list or dictionary and then we fetch it for required operations

m = [1, 2 , 5 ,6 ,1 ,2 ,5, 7, 9  ]
n = [5, 2 ,3 , 9, 1 ]

# in this we have to check how much time elements in n list come in m list so we have to return count, and if we solve using 2 for loop then it will give tle error if we check the constraint

#00 so to solve this issue we can first make the list or dictionary to store the count of number

# in constraint it is given that number can only in between 0 to 10

hash_list = [0]*11
for num in m:
    hash_list[num] += 1
    
for num in n:
    print(hash_list[num])
    
# Here time complexity would reduced to O(n*m)    
