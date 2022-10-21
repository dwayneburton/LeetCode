class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i, key in enumerate(nums):
            if target - key in mapping:
                return [mapping.get(target - key), i]
            else:
                mapping[key] = i