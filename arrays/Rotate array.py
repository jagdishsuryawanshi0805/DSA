class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        def reverse(left,right):
            while left<right:
                nums[left], nums[right] = nums[right],nums[left]
                left+=1 
                right-=1
        reverse(0 , len(nums)-1)
        reverse(0 , k-1)
        reverse(k , len(nums)-1)
sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7],3))