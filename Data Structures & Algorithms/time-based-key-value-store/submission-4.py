class TimeMap:
    def __init__(self):
        self.table = defaultdict(list)        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        arr = self.table[key]
        # print(timestamp, arr)
        left, right = 0, len(arr)-1
        greatest_timestamp = -1
        while right >= left:
            mid = (left+right) // 2
            if arr[mid][1] <= timestamp: 
                greatest_timestamp = mid
            if arr[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if greatest_timestamp == -1:
            return ""
        return arr[greatest_timestamp][0]
