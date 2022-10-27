class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits_list = []
        for digit in str(num):
            digits_list.append(int(digit))
        digits_list.sort()
        return digits_list[0]*10 + digits_list[2] + digits_list[1]*10 + digits_list[3]