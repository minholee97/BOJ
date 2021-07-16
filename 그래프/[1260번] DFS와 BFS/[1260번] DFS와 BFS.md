#  [BOJ] 1260번 : DFS와 BFS

## BOJ: https://www.acmicpc.net/problem/1260

## 1. 문제

|시간 제한| 메모리 제한| 
|:----|:----|
|2초|128MB|

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

#### 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

#### 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

#### 예제 입력 1
```
4 5 1
1 2
1 3
1 4
2 4
3 4
```
#### 예제 출력 1
```
1 2 4 3
1 2 3 4
```
## 2. 풀이
- 정점과 간선을 입력받아 각각 dfs와 bfs로 탐색을 진행.
- 간선이 양방향임에 주의.
- 정점의 번호가 작은 것을 먼저 방문함에 주의.

## 3. 작성 답안
```python
import sys
from collections import deque

def dfs():
	if len(q) == 0:
		return
	c = q.popleft()
	result.append(c)
	for i in range(len(edge[c])):
		t = edge[c][i]
		if visited[t] == False:
			visited[t] = True
			q.append(t)
			dfs()

def bfs():
	while True:
		if len(q) == 0:
			return
		c = q.popleft()
		result.append(c)
		for i in range(len(edge[c])):
			t = edge[c][i]
			if visited[t] == False:
				visited[t] = True
				q.append(t)

N, M, V = map(int, sys.stdin.readline().split())

edge = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
	st, ds = map(int, sys.stdin.readline().split())
	edge[st].append(ds)
	edge[ds].append(st)

for i in range(1, N + 1):
	edge[i].sort()

result = []
q = deque()
q.append(V)
visited[V] = True
dfs()
print(*result)

result = []
q = deque()
q.append(V)
visited = [False for _ in range(N + 1)]
visited[V] = True
bfs()
print(*result)
```
```cpp
#include <bits/stdc++.h>

using namespace std;

vector<int>* edge;
bool* visited;
	
deque<int> deq_d;
deque<int> deq_b;	

void dfs() {
	if (deq_d.size() == 0) {
		return;
	}
	int c = deq_d.front();
	printf("%d ", c);
	deq_d.pop_front();
	for (int i = 0; i < edge[c].size(); i++) {
		if (visited[edge[c][i]] == false) {
			visited[edge[c][i]] = true;
			deq_d.push_back(edge[c][i]);
			dfs();
		}
	}
}

void bfs() {
	while (true) {
		if (deq_b.size() == 0) {
			return;
		}
		int c = deq_b.front();
		printf("%d ", c);
		deq_b.pop_front();
		for (int i = 0; i < edge[c].size(); i++) {
			if (visited[edge[c][i]] == false) {
				visited[edge[c][i]] = true;
				deq_b.push_back(edge[c][i]);
			}
		}
	}
}

int main() {
	int N, M, V;
	scanf("%d %d %d", &N, &M, &V);
	edge = new vector<int>[N + 1];
	visited = new bool[N + 1];
	for (int i = 0; i < M; i++) {
		int st, ds;
		scanf("%d %d", &st, &ds);
		edge[st].push_back(ds);
		edge[ds].push_back(st);
	}
	
	for (int i = 1; i < N + 1; i++) {
		sort(edge[i].begin(), edge[i].end());
	}
	deq_d.push_back(V);
	deq_b.push_back(V);
	fill_n(visited, N + 1, false);
	visited[V] = true;
	dfs();
	printf("\n");
	fill_n(visited, N + 1, false);
	visited[V] = true;
	bfs();
	printf("\n");
}
```
## 4. 기타
- 경로가 중요한 것이 아니라 탐색되는 정점이 중요하므로 정점을 중복선택하지 않아야 시간을 줄일 수 있다.
- 그래프 문제를 풀 때 문제의 요구를 정확히 파악한다.
