import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap (store negative distance to simulate max-heap)
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)  # no need for sqrt
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for (_, point) in heap]
