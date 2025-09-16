# Selection Sort
def selection_sort(nums):
  n = len(nums)
  for i in range(0,n):
    min_index = i
    for j in range(i+1,n):
      if nums[j] < nums[min_index]:
        min_index = j
    nums[i],nums[min_index] = nums[min_index],nums[i]

# Here time complexity would be O(n*(n+1))/2 approximately equal to O(n^2)
# and space complexity is O(1) as we are not using any extra space 
