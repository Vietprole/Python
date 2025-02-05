from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        # Solution 2
        # nums_1 = [target - num for num in nums if num != target - num or nums.count(num) == 2]
        # result = []
        # for num in nums:
        #     if num in nums_1:
        #         temp = nums.index(num)
        #         result.append(temp)
        #         nums[temp] = None
        # return result

        # Solution 3
        dict_diff = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_diff:
                return nums.index(diff), i
            else:
                dict_diff[num] = diff