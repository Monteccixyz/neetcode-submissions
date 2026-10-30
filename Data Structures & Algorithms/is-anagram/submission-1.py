class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        seen = {}
        seen_2 = {}

        for n in s:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        for n in t:
            if n in seen_2:
                seen_2[n] += 1
            else:
                seen_2[n] = 1

        return seen == seen_2

        