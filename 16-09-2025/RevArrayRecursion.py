# We have to reverse an array using recursion and in the input We
# have given an array and two varial left and right from which we have to reverse

def reverse_array(nums,left,right):
    if left>=right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    
    reverse_array(nums,left+1,right-1)
    
    
# here time complexity would be O(N/2) approximately equal to O(n)
# as here we are doing half operations
# and space complexity would also be O(n/2) approximately equal to O(n)
