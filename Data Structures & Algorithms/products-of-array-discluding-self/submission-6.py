class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        right = [1] * l
        result = [1]*l

        for i in range(1,l):
            result[i] = result[i-1] * nums[i-1]
        
        for i in range(l - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        
        for i in range(l):
            result[i] = result[i]*right[i]
        return result
        