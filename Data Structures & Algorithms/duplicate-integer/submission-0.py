class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}

        for v in nums:
            if v in count_dict:
                count_dict[v]+=1
                return True
            else:
                count_dict[v]=1
        return False
        
