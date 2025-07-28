class Solution(object):
    def majorityElement(self, nums):
        # Create an empty dictionary (hash map) to count occurrences of each number
        count_map = {}
        # Loop through each number in the array
        for num in nums:
            # If the number is already in the dictionary, increase its count
            if num in count_map:
                count_map[num] += 1
            else:
                # If it's not in the dictionary, add it with count = 1
                count_map[num] = 1
            # Check immediately if this number has become the majority
            # Majority means count > n // 2
            if count_map[num] > len(nums) // 2:
                return num  # As soon as we find it, return it
