class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1 ==============
        # return len(s) == len(t) and "".join(sorted(.lower())) == "".join(sorted(t.lower()))
        # solution 2 hash table =============
        # if len(s) != len(t):
        #     return False
        # ht1 = {}
        # ht2 = {}
        # for i in range(len(s)):
        #     ht1[s[i]] = 1 + ht1.get(s[i], 0)
        #     ht2[t[i]] = 1 + ht2.get(t[i], 0)
        # return ht1 == ht2
        # solution 3 array bcoz of fixed lowercase characters
        if len(s) != len(t):
            return False
        
        countArr = [0] * 26
        for i in range(len(s)):
            countArr[ ord(s[i]) - ord('a') ] += 1
            countArr[ ord(t[i]) - ord('a') ] -= 1
        
        for val in countArr:
            if val != 0:
                return False
        return True