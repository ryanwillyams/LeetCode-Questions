class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for x in range(m , m+n):
            nums1.remove(0)
        nums1.extend(nums2)
        nums1.sort()

        