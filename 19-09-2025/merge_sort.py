# merge sort
# In this alogorithm we use divide and conquer technique

def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
        
        while j<m:
            result.append(right[j])
            j+=1
    return result
    
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge_array(left_arr,right_arr)
    
    
# time complexity would be O(nlogn)
# and space complexity would be O(N) as we are creating new array result
    
    
    
            
