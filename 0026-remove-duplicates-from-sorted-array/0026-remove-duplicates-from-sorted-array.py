class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = list(set(nums))
        length = len(mySet)
        mySet.sort()
        index = 0
        for x in mySet:
            nums[index] = x
            index +=1
        
        return length
            
