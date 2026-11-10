import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        time = 0
        visited = set() 
        heap = [(0, k)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(w1, time)
            for n2, w2 in edges[n1]:
                heapq.heappush(heap, (w2 + w1, n2))
        if len(visited) != n:
            return -1
        return time