#
# [1] Two Sum
#

class Solution(object):
    def twoSum(self, nums, target):

        for i, num in enumerate(nums):

            other = target - num

            if other in nums and nums.index(other) != i:
                return [i, nums.index(other)]
