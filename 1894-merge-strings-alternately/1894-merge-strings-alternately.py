class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        x = 0
        for x in range(len(word1)):
            merged += word1[x]
            if x < len(word2): merged += word2[x]

        if len(word1) < len(word2): merged+= word2[x+1:]
        return merged
            