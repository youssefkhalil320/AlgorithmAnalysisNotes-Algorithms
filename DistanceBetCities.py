import heapq
def manhattanDist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
def prime(src, graph, n):
    seen = set()
    minHeap = [[0, src]]  # pair of (dist, vertex)
    totalDist = 0
    while len(seen) < n:
        dist, u = heapq.heappop(minHeap)
        if u in seen: continue  # skip if this node is already included in MST
        seen.add(u)  # add this node to MST
        totalDist += dist
        for v, d in graph[u]:
            if v not in seen:
                heapq.heappush(minHeap, [d, v])
    return totalDist

def minCostConnectPoints(points):
    n = len(points)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = manhattanDist(points[i], points[j])
            graph[i].append([j, dist])
            graph[j].append([i, dist])
    
    return prime(0, graph, n)
    
if __name__ == '__main__':
    cities = [[0,0],[2,2],[3,10],[5,2],[7,0]]  # -> 20
    #cities = [[3,12],[-2,5],[-4,1]]  -> 18
    print(minCostConnectPoints(cities))
    