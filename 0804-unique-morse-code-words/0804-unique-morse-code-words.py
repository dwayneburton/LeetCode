class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsecode_map = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                         "e": ".", "f": "..-.", "g": "--.", "h": "....",
                         "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                         "m": "--", "n": "-.", "o": "---", "p": ".--.",
                         "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                         "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                         "y": "-.--", "z": "--.."}
        translations = set()
        for word in words:
            translation_temp = ""
            for letter in word:
                translation_temp += morsecode_map.get(letter)
            translations.add(translation_temp)
        return len(translations)