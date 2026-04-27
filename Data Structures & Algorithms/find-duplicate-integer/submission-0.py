class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        most=Counter(nums)
        res = 0
        for key,val in most.items():
            if val >=2:
                res = key
        return res
        