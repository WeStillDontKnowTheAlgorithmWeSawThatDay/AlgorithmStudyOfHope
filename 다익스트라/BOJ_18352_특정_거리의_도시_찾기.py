import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
INF = 1e8

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(x)

answer = []

for idx, val in enumerate(distance):
    if val == k:
        answer.append(idx)

print(-1 if len(answer) == 0 else '\n'.join(list(map(str, answer))))

