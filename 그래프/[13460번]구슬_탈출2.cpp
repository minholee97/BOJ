// https://www.acmicpc.net/problem/13460

#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

typedef struct Node {
	int rx, ry, bx, by, ox, oy;
	char str[10][10] = { '\0', };
	int count = 0;
	int dir = 0;
}node;

int main()
{
	int N, M;
	cin >> N >> M;
	char str[10][10] = { '\0', };
	node first;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> first.str[i][j];
			if (first.str[i][j] == 'R')
			{
				first.rx = i;
				first.ry = j;
			}
			else if (first.str[i][j] == 'B')
			{
				first.bx = i;
				first.by = j;
			}
			else if (first.str[i][j] == 'O')
			{
				first.ox = i;
				first.oy = j;
			}
		}
	}
	queue<node> q;
	q.push(first);
	int count = 0;
	int clear = 0;
	while (true)
	{
		if (q.front().dir != 1 && (q.front().str[q.front().rx][q.front().ry - 1] == '.' || q.front().str[q.front().bx][q.front().by - 1] == '.' || q.front().str[q.front().rx][q.front().ry - 1] == 'O' || q.front().str[q.front().bx][q.front().by - 1] == 'O'))
		{
			node temp;
			memcpy(&temp, &q.front(), sizeof(node));
			int f = 0;
			temp.count++;
			while (temp.str[temp.rx][temp.ry - 1] == '.' || temp.str[temp.bx][temp.by - 1] == '.' || temp.str[temp.rx][temp.ry - 1] == 'O' || temp.str[temp.bx][temp.by - 1] == 'O')
			{
				if (temp.str[temp.bx][temp.by - 1] == '.' || temp.str[temp.bx][temp.by - 1] == 'O')
				{
					swap(temp.str[temp.bx][temp.by], temp.str[temp.bx][temp.by - 1]);
					temp.by -= 1;
					if (temp.bx == temp.ox && temp.by == temp.oy)
					{
						temp.str[temp.bx][temp.by] = 'O';
						temp.str[temp.bx][temp.by + 1] = '.';
						f = 1;
						clear = 0;
						break;
					}
				}
				if (temp.str[temp.rx][temp.ry - 1] == '.' || temp.str[temp.rx][temp.ry - 1] == 'O')
				{
					swap(temp.str[temp.rx][temp.ry], temp.str[temp.rx][temp.ry - 1]);
					temp.ry -= 1;
					if (temp.rx == temp.ox && temp.ry == temp.oy)
					{
						temp.str[temp.rx][temp.ry] = 'O';
						temp.str[temp.rx][temp.ry + 1] = '.';
						clear = temp.count;
					}
				}
			}
			if (clear != 0)
			{
				cout << clear << endl;
				return 0;
			}
			temp.dir = 2;
			if (f != 1 && temp.count <= 10)
				q.push(temp);
		}
		if (q.front().dir != 2 && (q.front().str[q.front().rx][q.front().ry + 1] == '.' || q.front().str[q.front().bx][q.front().by + 1] == '.' || q.front().str[q.front().rx][q.front().ry + 1] == 'O' || q.front().str[q.front().bx][q.front().by + 1] == 'O'))
		{
			node temp;
			memcpy(&temp, &q.front(), sizeof(node));
			int f = 0;
			temp.count++;
			while (temp.str[temp.rx][temp.ry + 1] == '.' || temp.str[temp.bx][temp.by + 1] == '.' || temp.str[temp.rx][temp.ry + 1] == 'O' || temp.str[temp.bx][temp.by + 1] == 'O')
			{
				if (temp.str[temp.bx][temp.by + 1] == '.' || temp.str[temp.bx][temp.by + 1] == 'O')
				{
					swap(temp.str[temp.bx][temp.by], temp.str[temp.bx][temp.by + 1]);
					temp.by += 1;
					if (temp.bx == temp.ox && temp.by == temp.oy)
					{
						temp.str[temp.bx][temp.by] = 'O';
						temp.str[temp.bx][temp.by - 1] = '.';
						f = 1;
						clear = 0;
						break;
					}
				}
				if (temp.str[temp.rx][temp.ry + 1] == '.' || temp.str[temp.rx][temp.ry + 1] == 'O')
				{
					swap(temp.str[temp.rx][temp.ry], temp.str[temp.rx][temp.ry + 1]);
					temp.ry += 1;
					if (temp.rx == temp.ox && temp.ry == temp.oy)
					{
						temp.str[temp.rx][temp.ry] = 'O';
						temp.str[temp.rx][temp.ry - 1] = '.';
						clear = temp.count;
					}
				}
			}
			if (clear != 0)
			{
				cout << clear << endl;
				return 0;
			}
			temp.dir = 1;
			if (f != 1 && temp.count <= 10)
				q.push(temp);
		}
		if (q.front().dir != 3 && (q.front().str[q.front().rx - 1][q.front().ry] == '.' || q.front().str[q.front().bx - 1][q.front().by] == '.' || q.front().str[q.front().rx - 1][q.front().ry] == 'O' || q.front().str[q.front().bx - 1][q.front().by] == 'O'))
		{
			node temp;
			memcpy(&temp, &q.front(), sizeof(node));
			int f = 0;
			temp.count++;
			while (temp.str[temp.rx - 1][temp.ry] == '.' || temp.str[temp.bx - 1][temp.by] == '.' || temp.str[temp.rx - 1][temp.ry] == 'O' || temp.str[temp.bx - 1][temp.by] == 'O')
			{
				if (temp.str[temp.bx - 1][temp.by] == '.' || temp.str[temp.bx - 1][temp.by] == 'O')
				{
					swap(temp.str[temp.bx][temp.by], temp.str[temp.bx - 1][temp.by]);
					temp.bx -= 1;
					if (temp.bx == temp.ox && temp.by == temp.oy)
					{
						temp.str[temp.bx][temp.by] = 'O';
						temp.str[temp.bx + 1][temp.by] = '.';
						f = 1;
						clear = 0;
						break;
					}
				}
				if (temp.str[temp.rx - 1][temp.ry] == '.' || temp.str[temp.rx - 1][temp.ry] == 'O')
				{
					swap(temp.str[temp.rx][temp.ry], temp.str[temp.rx - 1][temp.ry]);
					temp.rx -= 1;
					if (temp.rx == temp.ox && temp.ry == temp.oy)
					{
						temp.str[temp.rx][temp.ry] = 'O';
						temp.str[temp.rx + 1][temp.ry] = '.';
						clear = temp.count;
					}
				}
			}
			if (clear != 0)
			{
				cout << clear << endl;
				return 0;
			}
			temp.dir = 4;
			if (f != 1 && temp.count <= 10)
				q.push(temp);
		}
		if (q.front().dir != 4 && (q.front().str[q.front().rx + 1][q.front().ry] == '.' || q.front().str[q.front().bx + 1][q.front().by] == '.' || q.front().str[q.front().rx + 1][q.front().ry] == 'O' || q.front().str[q.front().bx + 1][q.front().by] == 'O'))
		{
			node temp;
			memcpy(&temp, &q.front(), sizeof(node));
			int f = 0;
			temp.count++;
			while (temp.str[temp.rx + 1][temp.ry] == '.' || temp.str[temp.bx + 1][temp.by] == '.' || temp.str[temp.rx + 1][temp.ry] == 'O' || temp.str[temp.bx + 1][temp.by] == 'O')
			{
				if (temp.str[temp.bx + 1][temp.by] == '.' || temp.str[temp.bx + 1][temp.by] == 'O')
				{
					swap(temp.str[temp.bx][temp.by], temp.str[temp.bx + 1][temp.by]);
					temp.bx += 1;
					if (temp.bx == temp.ox && temp.by == temp.oy)
					{
						temp.str[temp.bx][temp.by] = 'O';
						temp.str[temp.bx - 1][temp.by] = '.';
						f = 1;
						clear = 0;
						break;
					}
				}
				if (temp.str[temp.rx + 1][temp.ry] == '.' || temp.str[temp.rx + 1][temp.ry] == 'O')
				{
					swap(temp.str[temp.rx][temp.ry], temp.str[temp.rx + 1][temp.ry]);
					temp.rx += 1;
					if (temp.rx == temp.ox && temp.ry == temp.oy)
					{
						temp.str[temp.rx][temp.ry] = 'O';
						temp.str[temp.rx - 1][temp.ry] = '.';
						clear = temp.count;
					}
				}
			}
			if (clear != 0)
			{
				cout << clear << endl;
				return 0;
			}
			temp.dir = 3;
			if (f != 1 && temp.count <= 10)
				q.push(temp);
		}
		q.pop();
		if (q.empty() == true || q.front().count == 10)
		{
			cout << "-1" << endl;
			return 0;
		}
	}
	return 0;
}
