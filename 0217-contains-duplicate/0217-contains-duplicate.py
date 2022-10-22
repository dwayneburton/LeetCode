class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping = {}
        for num in nums:
            if mapping.get(num):
                return True
            mapping[num] = True
        return False