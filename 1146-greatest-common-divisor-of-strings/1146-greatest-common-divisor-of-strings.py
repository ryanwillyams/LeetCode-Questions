class Solution:
    def computeGCD(self, x, y):
        x = y
       
        return abs(x)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divider = str1 if str1 < str2 else str2
        divided = str2 if str2 >= str1 else str1
        maxsub = ""
        maxiterations = self.computeGCD(len(divided), len(divider))
        for i in range(maxiterations):
            sub = divider[:i+1]
            countDivided = divided.count(sub)
            countDivider = divider.count(sub)
            if countDivided*(i+1) == len(divided) and countDivider*(i+1) == len(divider):
                maxsub = sub
        return maxsub