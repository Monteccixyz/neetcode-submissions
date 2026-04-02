class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # this is the start of a sequence
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)
        
        return best