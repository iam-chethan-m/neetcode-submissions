class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1] * l
        right = [1] * l

        # result = []

        # for i, v in enumerate(nums):
        #     idx = i + 1
        #     prod = 1
        #     for j in nums[: abs(idx - 1)] + nums[idx:]:
        #         prod *= j
        #     result.append(prod)

        for i in range(1,l):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(l - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # print(f"Left: {left} \nRight: {right}")

        result = [0]*l
        for i in range(l):
            result[i] = left[i]*right[i]
        return result
        