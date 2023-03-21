class Solution:
    def findMin(self, nums: list[int]) -> int:
        # way1
        # return min(nums) 時間複雜度為O(n)

        # way2用二分法
        res = float('inf')
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return res


# case1
# sol = Solution()
# res = sol.findMin([3, 4, 5, 1, 2])
# print(res)

# case2
sol = Solution()
res = sol.findMin([4, 5, 6, 7, 0, 1, 2])
print(res)

# # case3
# sol = Solution()
# res = sol.findMin([11, 13, 15, 17])
# print(res)
