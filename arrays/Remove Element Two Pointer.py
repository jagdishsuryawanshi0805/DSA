class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # pointer for the next position of non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # move the non-val element forward
                k += 1
        return k  # new length of modified array
