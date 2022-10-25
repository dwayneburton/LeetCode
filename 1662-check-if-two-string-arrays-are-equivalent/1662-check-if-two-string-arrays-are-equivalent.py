class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        string_1 = ''
        string_2 = ''
        for letters in word1:
            string_1 += letters
        for letters in word2:
            string_2 += letters
        return string_1 == string_2
            