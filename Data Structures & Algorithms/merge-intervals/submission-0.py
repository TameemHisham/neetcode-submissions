class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ptr1 = 0
        res = []
        while ptr1 < len(intervals):
            start= intervals[ptr1][0]
            end = intervals[ptr1][1]
            while ptr1+1 < len(intervals) and intervals[ptr1 + 1][0] <= end:
                end = max(end, intervals[ptr1 + 1][1])
                ptr1 += 1 
            res.append([start, end])
            ptr1 += 1 
        return res
