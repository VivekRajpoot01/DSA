# DSA Progress - Sorting Algorithms

## Today's Progress
Implemented two important sorting algorithms using the divide and conquer approach.

## 1. Merge Sort

### Algorithm Overview
- Uses divide and conquer technique
- Recursively splits the array into halves
- Merges sorted subarrays in correct order

### Implementation
```python
# In this algorithm we use divide and conquer technique

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
```

### Complexity Analysis
- **Time Complexity**: O(nlogn) in all cases
- **Space Complexity**: O(n) due to auxiliary arrays

## 2. Quick Sort

### Algorithm Overview
- Uses divide and conquer technique
- Selects a pivot element and partitions the array around it
- Recursively sorts subarrays on both sides of the pivot

### Implementation
```python
# In this algorithm
# First we have to pick a pivot element and it can be any element in the array
# And put pivot at its correct position/index

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i] <= pivot and i<=high-1:
            i+=1
        while nums[j] >= pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j], nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    return j
    
def quick_sort(nums,low,high):
    if low<high:
        p_ind = partition(nums,low,high)
        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)
    
    return nums
```

### Complexity Analysis
- **Average Time Complexity**: O(nlogn)
- **Worst-case Time Complexity**: O(n²)
- **Space Complexity**: O(logn) due to recursion stack

## Key Learnings
1. Understanding of divide and conquer paradigm
2. Differences between stable (Merge Sort) and unstable (Quick Sort) algorithms
3. Trade-offs between time and space complexity
4. Importance of pivot selection in Quick Sort
5. Recursive algorithm design and implementation

## Next Steps
1. Implement randomized pivot selection for Quick Sort
2. Analyze performance with different input types
3. Compare actual performance with theoretical complexity
4. Implement iterative versions of both algorithms

## Usage Example
```python
# Test Merge Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Merge sorted:", merge_sort(arr))

# Test Quick Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Quick sorted:", quick_sort(arr, 0, len(arr)-1))
```
