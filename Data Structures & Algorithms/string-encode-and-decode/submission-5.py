class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
          return ""
        
        encoded_strs = []
        for s in strs:
            if s == "":
                encoded_strs.append(":")
            else:
                encoded_strs.append("#".join(str(ord(c)) for c in s))
        # print(encoded_strs)

        return "|".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        
        if s=="":
            return []
        strs = s.split("|")
        decode_strs = []
        for s in strs:
            if s==":":
                decode_strs.append("")
            else:
                word = "".join(chr(int(x)) for x in s.split("#"))
                decode_strs.append(word)
        return decode_strs