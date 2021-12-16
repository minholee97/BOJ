#  [BOJ] 16929번 : Two Dots

## BOJ: https://www.acmicpc.net/problem/16929

## 1. 문제

|시간 제한| 메모리 제한| 
|:----|:----|
|2초|512MB|

Two Dots는 Playdots, Inc.에서 만든 게임이다. 게임의 기초 단계는 크기가 N×M인 게임판 위에서 진행된다.

각각의 칸은 색이 칠해진 공이 하나씩 있다. 이 게임의 핵심은 같은 색으로 이루어진 사이클을 찾는 것이다.

점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의는 아래와 같다.

- 모든 k개의 점은 서로 다르다. 
- k는 4보다 크거나 같다.
- 모든 점의 색은 같다.
- 모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 또, dk와 d1도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.

게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.

#### 입력
첫째 줄에 게임판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다. 게임판은 모두 점으로 가득차 있고, 게임판의 상태는 점의 색을 의미한다. 점의 색은 알파벳 대문자 한 글자이다.
- 2 ≤ N, M ≤ 50

#### 출력
사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.

#### 예제 입력 1
```
3 4
AAAA
ABCA
AAAA
```
#### 예제 출력 1
```
Yes
```
## 2. 풀이
- 그래프 내의 사이클을 찾는 문제
- 모든 지점에서 DFS를 수행하여 원래 위치로 돌아올 수 있는지를 확인
- 방문 노드와 온 방향으로 다시 돌아가는 것을 같이 체크
- 다음 노드가 자신과 같은 색인지 확인

## 3. 작성 답안
```python
import sys
from collections import deque

mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(d, p, c):
	for i in range(4):
		x = d[0] + mv[i][0]
		y = d[1] + mv[i][1]
		if 0 <= x < N and 0 <= y < M and mv[i] != p and bd[x][y] == c:
			if st == [x, y]:
				print("Yes")
				exit()
			if visited[x][y] == False:
				visited[x][y] = True
				dfs([x, y], [-mv[i][0], -mv[i][1]], c)
				visited[x][y] = False

N, M = map(int, sys.stdin.readline().split())

bd = []

for _ in range(N):
	line = list(sys.stdin.readline().rstrip())
	bd.append(line)

for i in range(N):
	for j in range(M):
		st = [i, j]
		visited = [[False for _ in range(M)] for _ in range(N)]
		visited[i][j] = True
		dfs([i, j], None, bd[i][j])
print("No")
```
## 4. 기타
- DFS
