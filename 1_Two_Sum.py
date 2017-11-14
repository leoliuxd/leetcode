class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            n1 = nums[i]
            n2 = target - n1
            if n2 in nums:
                if i + 1 < len(nums):
                    for j in range(i+1, len(nums)):
                        if nums[j] == n2:
                            return [i, j]