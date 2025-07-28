class Solution(object):
    def removeDuplicates(self, nums):
    
        # If the array has 2 or fewer elements, all are allowed
        if len(nums) <= 2:
            return len(nums)
        # Pointer 'i' points to the position where next allowed element goes
        i = 2  # Start from index 2 because the first two elements are always valid
        # Loop through from index 2 to the end
        for j in range(2, len(nums)):
            # Compare current number with the number 2 positions before
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]  # Place current number at position i
                i += 1             # Move i forward
        return i  # 'i' is the count of valid elements
