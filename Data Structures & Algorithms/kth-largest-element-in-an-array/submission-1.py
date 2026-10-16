import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if minHeap:
                while len(minHeap) > k:
                    heapq.heappop(minHeap)

            heapq.heappush(minHeap,n)
        
        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return heapq.heappop(minHeap)
