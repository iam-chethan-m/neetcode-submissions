from collections import defaultdict
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        result = []

        for n in nums:
            if n in count_dict:
                count_dict[n]+=1
            else:
                count_dict[n]=1
        count_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))

        for i in range(k):
            result.append(list(count_dict.keys())[i])

        return result
