class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = sorted(set(nums))
        length = len(mySet)
        index = 0
        for x in mySet:
            nums[index] = x
            index +=1
        
        return length
            
