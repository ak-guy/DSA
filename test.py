import heapq

class Comparator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __gt__(self, other):
        return self.x < other.x
    
    def __repr__(self):
        return f"{self.x}, {self.y}"

arr = [[1,2], [5,2], [2,8]]
pq = []
for val in arr:
    heapq.heappush(pq, Comparator(val[0], val[1]))
# heapq.heapify(arr, key=lambda x: arr[x[2]])

for _ in range(len(arr)):
    val = pq.pop()
    print(val)