from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)

        for i in range(len(s2)-len(s1)+1):
            if s2[i] in s1:
                seen = Counter(s1)
                count = 0
                for y in range(i,i+len(s1)):
                    if s2[y] not in seen:
                        break
                    if seen[s2[y]] == 0:
                        break
                    count += 1
                    seen[s2[y]] -= 1
                if count == len(s1):
                    return True

        return False

