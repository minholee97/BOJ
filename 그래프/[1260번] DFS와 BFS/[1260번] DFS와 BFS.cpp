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