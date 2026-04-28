class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i in range(len(nums)):
            diff = target -nums[i]
            if diff in hs:
                return [hs[diff], i]
            hs[nums[i]] = i