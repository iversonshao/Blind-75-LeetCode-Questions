class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 除了自己以外其他都要相乘，然後不能用除法，時間在O(n)
        # way1前面積成後面積
        if not nums:
            return []
        answers = [1 for i in range(len(nums))]
        prefixProduct = 1
        for i in range(len(nums)):
            answers[i] *= prefixProduct
            prefixProduct *= nums[i]

        postProduct = 1
        for j in range(len(nums)-1, -1, -1):
            answers[j] *= postProduct
            postProduct *= nums[j]

        return answers


# case1
# sol = Solution()
# res = sol.productExceptSelf([1, 2, 3, 4])
# print(res)

# case2
sol = Solution()
res = sol.productExceptSelf([-1, 1, 0, -3, 3])
print(res)
