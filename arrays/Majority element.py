class Solution(object):
    def majorityElement(self, nums):
        # Initialize a counter to track how many times our current candidate is "supported"
        count = 0
        # This will hold our current majority candidate
        candidate = None
        # Loop through every number in the array
        for num in nums:
            # If count is 0, we choose a new candidate
            if count == 0:
                candidate = num  # Pick the current number as the new candidate
            # If the current number is the same as our candidate, it's a vote for the candidate
            if num == candidate:
                count += 1  # Increase support count
            else:
                count -= 1  # Otherwise, it's a vote against the candidate
        # At the end, candidate will be the majority element
        return candidate
