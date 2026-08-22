import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(list)

        for i, item in enumerate(nums):
            if item in hashMap:
                hashMap[item] += 1
            else:
                hashMap[item] = 1
        
        count = Counter(hashMap)

        top_k = heapq.nlargest(k, hashMap, hashMap.get)

        return top_k
        