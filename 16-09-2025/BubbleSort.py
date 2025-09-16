# Here we will write bubble sort code

def bubble_sort(nums):
  n = len(nums)
  for i in range(n-2,-1,-1):
    is_swap = False
    for j in range(0,i+1):
      if(nums[j]>nums[j+1]):
        nums[j],nums[j+1] = nums[j+1],nums[j]
        is_swap = True

    if is_swap == False:
      return


# For average and worst case time complexity would be O(n*(n+1))/2 approximately equal to O(n^2)
# for best case time complexity would be O(n) as we are using is_swap variable to check do we realy required swapping
# And the space complexity is again O(1) as we are not using any extra space 
