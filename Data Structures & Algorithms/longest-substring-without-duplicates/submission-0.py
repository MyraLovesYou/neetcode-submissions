class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = {}  
        for i, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = i
            max_len = max(max_len, i - left + 1)
            
        return max_len