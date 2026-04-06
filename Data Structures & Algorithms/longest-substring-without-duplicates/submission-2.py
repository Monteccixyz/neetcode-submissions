class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bank = {}
        left = 0
        best = 0
        for i, char in enumerate(s):
            if char in bank and bank[char] >= left:
                left = bank[char] + 1
            bank[char] = i
            best = max(best, i - left + 1)
        return best