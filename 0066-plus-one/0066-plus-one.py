class Solution(object):
    def baseTen(self, digits, index):
        if index < 0:
            digits[0] = 1
            digits.append(0)
            return digits
        if digits[index] <= 8:
            digits[index] += 1
            return digits
        digits[index] = 0
        return self.baseTen(digits, index - 1)
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return self.baseTen(digits, len(digits) - 1)