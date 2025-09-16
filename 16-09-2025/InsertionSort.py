# we will be writing code for insertion sort

def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>=key:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = key  
        
# Here time complexity would be O(n*(n+1))/2 which is approximately equal to O(n^2)
# and space complexity is O(1)
