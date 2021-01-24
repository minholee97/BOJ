// https://www.acmicpc.net/problem/1004

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
		int x1, y1, x2, y2, p_amount, count = 0;
		cin >> x1 >> y1 >> x2 >> y2;
		cin >> p_amount;
		vector<vector<int>> planet(p_amount, vector<int>(3, 0));
		for (int i = 0; i < p_amount; i++)
		{
			cin >> planet[i][0] >> planet[i][1] >> planet[i][2];
		}
		for (int j = 0; j < p_amount; j++)
		{
			if (sqrt(pow(x1 - planet[j][0], 2) + pow(y1 - planet[j][1], 2)) < planet[j][2] && sqrt(pow(x2 - planet[j][0], 2) + pow(y2 - planet[j][1], 2)) > planet[j][2])
				count++;
			else if (sqrt(pow(x1 - planet[j][0], 2) + pow(y1 - planet[j][1], 2)) > planet[j][2] && sqrt(pow(x2 - planet[j][0], 2) + pow(y2 - planet[j][1], 2)) < planet[j][2])
				count++;
		}
		sol.push_back(count);
	}
	for (int i = 0; i < sol.size(); i++)
	{
		cout << sol.at(i) << endl;
	}
}