def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False

        # we can also solve the question with the help of hash set in O(n) time complexity 
        #but it increases the space complexity to O(n) as we are using the hash set to store the number
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        """
                
