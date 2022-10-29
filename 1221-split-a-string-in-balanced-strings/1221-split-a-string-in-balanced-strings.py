class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balanced, l_count, r_count = 0, 0, 0
        for char in s:
            if char == 'L':
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                balanced += 1
                r_count, l_count = 0, 0
        return balanced