from _heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        while k > 1:
            k-= 1
            heappop(maxHeap)
        return -heappop(maxHeap)