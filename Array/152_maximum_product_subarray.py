class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # 判斷負數個數與0的個數
        # 如果遇到0，把前面的數POP出來，再繼續算，遇到負數，看這一串數字中有幾個負數
        # way1暴力全部相乘輸出最大值
        # product = [[0] * len(nums) for i in range(len(nums))]
        # for i in range(0, len(nums)):
        #     for j in range(i, len(nums)):
        #         if i == j:
        #             product[i][j] = nums[i]
        #         else:
        #             product[i][j] = product[i][j-1] * nums[j]

        # return max(map(max, product))

        # way2 DP
        ans = nums[0]
        cur_min = nums[0]  # 紀錄當前最小值
        cur_max = nums[0]  # 紀錄當前最大值

        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = cur_min
                cur_min = cur_max
                cur_max = temp
            cur_min = min(cur_min * nums[i], nums[i])
            cur_max = max(cur_max * nums[i], nums[i])
            ans = max(ans, cur_max)
        return ans


# case1
sol = Solution()
res = sol.maxProduct([2, 3, -2, 4])
print(res)

# case2
# sol = Solution()
# res = sol.maxProduct([-2, 0, -1])
# print(res)


# sol = Solution()
# res = sol.maxProduct([-3, -1, -1])
# print(res)
