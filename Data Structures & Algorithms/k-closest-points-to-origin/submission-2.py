class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        # Calculate distances
        for i,(x,y) in enumerate(points):
            distances.append((-math.sqrt((x)**2 + (y)**2),i))
        # Add to max heap
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        return [points[i] for _,i  in distances]
        
        