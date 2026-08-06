class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx1 = None
        idx2 = None

        for i in range(len(nums)):
            diff = target - nums[i]
            idx1 = i
            if diff in nums:
                for j in range(len(nums)):
                    if diff == nums[j] and idx1!=j:
                        return [idx1, j]