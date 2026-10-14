import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use negative values to simulate max-heap
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)  # largest
            second = -heapq.heappop(maxHeap) # second largest
            if first != second:
                heapq.heappush(maxHeap, -(first - second))

        return -maxHeap[0] if maxHeap else 0
