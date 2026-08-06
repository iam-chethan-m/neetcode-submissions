from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angram_dict = defaultdict(list)
        output = []

        for s in strs:
            sorted_s = tuple(sorted(s))

            angram_dict[sorted_s].append(s)

        for value in angram_dict.values():
            output.append(value)

        return output