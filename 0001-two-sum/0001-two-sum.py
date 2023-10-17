class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look = {}
        for x in range(len(nums)):
            if target - nums[x] in look :
                return look[target - nums[x]], x
            look[nums[x]] = x

         
        
        
        