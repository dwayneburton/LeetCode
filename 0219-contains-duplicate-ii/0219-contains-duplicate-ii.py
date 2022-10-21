class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = {}
        for i, num in enumerate(nums):
            if num in mapping and abs(mapping[num] - i) <= k:
                return True
            mapping[num] = i
        return False