from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.get(nums[i]) != None:
                return [dictionary.get(nums[i]), i]
            dictionary[target - nums[i]] = i
        return []