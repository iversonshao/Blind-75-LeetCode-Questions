# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # way1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # way2 hashtable
        d = {}
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in d:
                return [d[num2], i]
            d[num1] = i


# case1
sol = Solution()
res = sol.twoSum([2, 7, 11, 15], 26)
print(res)

# case2
# sol = Solution()
# res = sol.twoSum([3, 2, 4], 6)
# print(res)


# case3
# sol = Solution()
# res = sol.twoSum([3, 3], 6)
# print(res)
