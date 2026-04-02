
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        ordered = sorted(nums)
        res = list(dict.fromkeys(ordered))

        current = 1
        best = 1
        for i in range(len(res)-1):
            if res[i+1] == res[i]+1:
                current += 1
                best = max(best, current)
            else:
                current = 1
                
        return best

