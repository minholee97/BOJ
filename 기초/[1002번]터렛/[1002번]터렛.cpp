// https://www.acmicpc.net/problem/1002

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main() 
{
	int loop;
	vector<int> sol;
	cin >> loop;
	while (loop--)
	{
		double x1, y1, r1, x2, y2, r2, dist;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
		if (r1 > r2)
		{
			if (dist == 0)
				sol.push_back(0);
			else if (dist < r1)
			{
				if (dist + r2 < r1)
					sol.push_back(0);
				else if (dist + r2 == r1)
					sol.push_back(1);
				else
					sol.push_back(2);
			}
			else if (dist == r1)
				sol.push_back(2);
			else
			{
				if (r1 + r2 < dist)
					sol.push_back(0);
				else if (r1 + r2 == dist)
					sol.push_back(1);
				else
					sol.push_back(2);
			}
		}
		else if (r1 == r2)
		{
			if (dist == 0)
				sol.push_back(-1);
			else if (dist < (r1 + r2))
				sol.push_back(2);
			else if (dist == (r1 + r2))
				sol.push_back(1);
			else
				sol.push_back(0);
		}
		else
		{
			if (dist == 0)
				sol.push_back(0);
			else if (dist < r2)
			{
				if (dist + r1 < r2)
					sol.push_back(0);
				else if (dist + r1 == r2)
					sol.push_back(1);
				else
					sol.push_back(2);
			}
			else if (dist == r2)
				sol.push_back(2);
			else
			{
				if (r1 + r2 < dist)
					sol.push_back(0);
				else if (r1 + r2 == dist)
					sol.push_back(1);
				else
					sol.push_back(2);
			}

		}

	}
	for (int i = 0; i < sol.size(); i++)
	{
		cout << sol.at(i) << endl;
	}
}