class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 給一個array，回傳一段連續總和的最大值
        # 每個ele去看，如果選自己是最大值，則選自己，如果不是擇選擇要不要選前面一個
        # way:DP的方法去解
        subArray = [0 for i in range(len(nums))]
        subArray[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= subArray[i-1]:
                temp = 0
                temp = nums[i] + subArray[i-1]
                if nums[i] >= temp:
                    subArray[i] = nums[i]
                else:
                    subArray[i] = temp

            else:
                subArray[i] = subArray[i-1] + nums[i]
        return max(subArray)


# case1
# sol = Solution()
# res = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(res)

# case2
# sol = Solution()
# res = sol.maxSubArray([1])
# print(res)

# case3
# sol = Solution()
# res = sol.maxSubArray([5, 4, -1, 7, 8])
# print(res)
