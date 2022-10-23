class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        twice = []
        for num in nums:
            if num in s:
                twice.append(num)
            else:
                s.add(num)
        return twice