// https://www.acmicpc.net/problem/13023

#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int>* rel;
int* visited;
int flag = 0;

void dfs(int p, int c){
	visited[p] = 1;
	c++;
	if (c == 5) {
		flag = 1;
		return;
	}
	for (int i = 0; i < rel[p].size(); i++){
		int next = rel[p][i];
		if (visited[next] == 0) {
			dfs(next, c);
			if (flag == 1)
				return;
			visited[next] = 0;
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &M);
	
	rel = new vector<int>[N];
	visited = new int[N];
	fill_n(visited, N, 0);
	
	int s, d;
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &s, &d);
		rel[s].push_back(d);
		rel[d].push_back(s);
	}
	
	for (int i = 0; i < N; i++) {
		dfs(i, 0);
		if (flag == 1){
			printf("1\n");
			break;
		}
		fill_n(visited, N, 0);
	}
	if (flag != 1)
		printf("0\n");
}