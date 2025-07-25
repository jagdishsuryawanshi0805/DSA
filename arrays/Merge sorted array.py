class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Last real element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last index of nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
