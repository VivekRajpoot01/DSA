## we have give an integer n (size of the array) and after that elements in the array
## and we have to count how many times each integer occur

def countInteger(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    for num in freq:
        print(f"{num} occures {freq[num]} times")
            
n = int(input())
list = input().split()
arr = [int(x) for x in list]
countInteger(arr)
