class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            temp = 0
            for i in [int(x) for x in str(n)]:
                temp += (i*i)
                
           
            n = temp
        
        return True