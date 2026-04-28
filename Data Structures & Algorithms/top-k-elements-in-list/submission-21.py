class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        newArray = []
        for key, val in count.items():
            newArray.append((val,key))
        newArray.sort()
        res = []
        while len(res)<k:
            res.append(newArray.pop()[1])
        return res