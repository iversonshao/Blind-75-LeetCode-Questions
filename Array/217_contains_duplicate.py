class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # way1暴力法
        # counts = 0
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             counts += 1
        #             break

        # if counts > 0:
        #     return True
        # else:
        #     return False
        # way2 set()
        # return len(set(nums)) != len(nums)
        # way3 hashtable
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                return hashmap.get(i)
            else:
                hashmap[i] = True
        return False


# case1
# sol = Solution()
# res = sol.containsDuplicate([1, 2, 3, 1])
# print(res)


# case2
# sol = Solution()
# res = sol.containsDuplicate([1, 2, 3, 4])
# print(res)

# case3
# sol = Solution()
# res = sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
# print(res)
