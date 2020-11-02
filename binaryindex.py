class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1 #0, 3
        while lo <= hi:
            mid = (lo + hi) // 2 #3//2 = 1
            if nums[mid] == target: #false
                return mid
            if nums[mid] >= nums[lo]: #nums[mid] = 1 >= nums[lo] = 100
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

s = Solution()
print(s.search([100, 1, 2, 3], 3))