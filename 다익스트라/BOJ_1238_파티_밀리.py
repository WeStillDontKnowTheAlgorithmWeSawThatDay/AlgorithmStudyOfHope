import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, pos = heapq.heappop(q)
        if distance[pos] < dist:
            continue
        for i in graph[pos]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

student = [-1] * (n + 1)
for i in range(1, n + 1):
    distance = dijkstra(i)
    student[i] = distance[x]

distance = dijkstra(x)
for i in range(1, n + 1):
    student[i] += distance[i]

print(max(student))