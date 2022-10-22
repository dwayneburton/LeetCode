class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping = {}
        for num in nums:
            mapping[num] = True
        return len(mapping) < len(nums)