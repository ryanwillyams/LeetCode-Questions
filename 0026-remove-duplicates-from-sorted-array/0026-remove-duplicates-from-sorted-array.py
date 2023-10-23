class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = sorted(set(nums))
        length = len(mySet)
        index = 0
        nums[:] = mySet
        
        return length
            
