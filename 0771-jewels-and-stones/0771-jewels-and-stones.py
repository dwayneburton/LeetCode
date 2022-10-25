class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = 0
        s = set()
        for jewel in jewels:
            s.add(jewel)
        for stone in stones:
            if stone in s:
                counter += 1
        return counter