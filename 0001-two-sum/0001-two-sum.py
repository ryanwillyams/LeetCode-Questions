class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look = {}
        for x in range(len(nums)):
            temp = target - nums[x]
            if temp in look :
                return look[target - nums[x]], x
            look[nums[x]] = x

         
        
        
        