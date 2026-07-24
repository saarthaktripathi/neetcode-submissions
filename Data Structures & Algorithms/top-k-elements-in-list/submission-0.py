class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s= defaultdict(list)
        for i in nums:
            s[i].append(i)
        s =sorted(s.items(),key=lambda item:len(item[1]))
        ss= dict(s)
        return(list(ss.keys()))[-k:]