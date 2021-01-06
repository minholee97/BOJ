//https://www.acmicpc.net/problem/12100

#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

typedef struct State {
	int bd[20][20] = { 0, };
	int mCount = 0;

}state;

int main()
{
	int N;
	cin >> N;
	state init;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> init.bd[i][j];
		}
	}
	queue<state> q;
	q.push(init);
	int max = 0;
	while (true)
	{
		state up, down, left, right;
		memcpy(&up, &q.front(), sizeof(state));
		memcpy(&down, &q.front(), sizeof(state));
		memcpy(&left, &q.front(), sizeof(state));
		memcpy(&right, &q.front(), sizeof(state));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N - 1; j++)
			{
				for (int k = j + 1; k < N; k++)
				{
					if (up.bd[j][i] == up.bd[k][i])
					{
						up.bd[j][i] = up.bd[j][i] + up.bd[k][i];
						up.bd[k][i] = 0;
						break;
					}
					if (up.bd[j][i] < up.bd[k][i] || up.bd[k][i] != 0)
						break;
				}
				for (int k = j + 1; k < N; k++)
				{
					if (left.bd[i][j] == left.bd[i][k])
					{
						left.bd[i][j] = left.bd[i][j] + left.bd[i][k];
						left.bd[i][k] = 0;
						break;
					}
					if (left.bd[i][j] < left.bd[i][k] || left.bd[i][k] != 0)
						break;
				}
			}
			for (int j = 0; j < N - 1; j++)
			{
				if (up.bd[j][i] == 0)
				{
					for (int k = j + 1; k < N; k++)
					{
						if (up.bd[k][i] != 0)
						{
							up.bd[j][i] = up.bd[k][i];
							up.bd[k][i] = 0;
							break;
						}
					}
				}
				if (left.bd[i][j] == 0)
				{
					for (int k = j + 1; k < N; k++)
					{
						if (left.bd[i][k] != 0)
						{
							left.bd[i][j] = left.bd[i][k];
							left.bd[i][k] = 0;
							break;
						}
					}
				}
			}
			for (int j = N - 1; j > 0; j--)
			{
				for (int k = j - 1; k > -1; k--)
				{
					if (down.bd[j][i] == down.bd[k][i])
					{
						down.bd[j][i] = down.bd[j][i] + down.bd[k][i];
						down.bd[k][i] = 0;
						break;
					}
					if (down.bd[j][i] < down.bd[k][i] || down.bd[k][i] != 0)
						break;
				}
				for (int k = j - 1; k > -1; k--)
				{
					if (right.bd[i][j] == right.bd[i][k])
					{
						right.bd[i][j] = right.bd[i][j] + right.bd[i][k];
						right.bd[i][k] = 0;
						break;
					}
					if (right.bd[i][j] < right.bd[i][k] || right.bd[i][k] != 0)
						break;
				}
			}
			for (int j = N - 1; j > 0; j--)
			{
				if (down.bd[j][i] == 0)
				{
					for (int k = j - 1; k > -1; k--)
					{
						if (down.bd[k][i] != 0)
						{
							down.bd[j][i] = down.bd[k][i];
							down.bd[k][i] = 0;
							break;
						}
					}
				}
				if (right.bd[i][j] == 0)
				{
					for (int k = j - 1; k > -1; k--)
					{
						if (right.bd[i][k] != 0)
						{
							right.bd[i][j] = right.bd[i][k];
							right.bd[i][k] = 0;
							break;
						}
					}
				}
			}
			for (int j = 0; j < N; j++)
			{
				if (max < up.bd[j][i])
					max = up.bd[j][i];
				if (max < left.bd[i][j])
					max = left.bd[i][j];
				if (max < down.bd[N - 1 - j][i])
					max = down.bd[N - 1 - j][i];
				if (max < right.bd[i][N - 1 - j])
					max = right.bd[i][N - 1 - j];
			}
		}
		if (q.front().mCount < 4)
		{
			up.mCount++;
			left.mCount++;
			down.mCount++;
			right.mCount++;
			q.push(up);
			q.push(left);
			q.push(down);
			q.push(right);
		}
		q.pop();
		if (q.empty() == true)
			break;
	}
	cout << max << endl;

	return 0;
}
