class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heaviest so max heap 

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y,x  = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if x == y:
                continue
            if x < y:
                heapq.heappush(maxHeap, -(y-x))
        return -maxHeap[0] if len(maxHeap) else 0 