import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict: dict = defaultdict(int)
        t_dict: dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1
        for key, val in s_dict.items():
            if t_dict[key] != val:
                return False
        return True