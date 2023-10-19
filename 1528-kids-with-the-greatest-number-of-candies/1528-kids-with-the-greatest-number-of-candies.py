class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       
        torF = [0] * len(candies)
       
        for x in range(len(candies)):
          
            if candies[x] + extraCandies  >= max(candies):
                torF[x] = True
            else: torF[x] = False
        
        return torF
            
            
