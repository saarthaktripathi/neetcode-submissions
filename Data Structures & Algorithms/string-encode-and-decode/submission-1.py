class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "~"
        s1 = ""
        for word in strs:
            s1 = s1 + word
            s1 = s1 + delimiter
        return s1


    def decode(self, s: str) -> List[str]:
        delimiter = "~"
        strs = []
        word = ""
        for letter in s:
            if letter == delimiter:
                strs.append(word)
                word = ""
                continue
            word = word + letter

        return strs