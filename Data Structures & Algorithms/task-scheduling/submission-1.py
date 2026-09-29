class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap: List[int] = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        cooldownQueue = deque()
        time = 0
        while cooldownQueue or maxHeap:
            time += 1
            if not maxHeap:
                time = cooldownQueue[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    cooldownQueue.append([count, time+n])
            if cooldownQueue and cooldownQueue[0][1] == time:
                heapq.heappush(maxHeap, cooldownQueue.popleft()[0])
        return time
                
                
            

            

