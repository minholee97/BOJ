// https://www.acmicpc.net/problem/1003

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
		int n, num_0 = 1, num_1 = 1, temp_num = 0;
		cin >> n;
		if (n == 0)
		{
			sol.push_back(1);
			sol.push_back(0);
		}
		else if (n == 1)
		{
			sol.push_back(0);
			sol.push_back(1);
		}
		else
		{
			for (int i = 0; i < n - 2; i++)
			{
				temp_num = num_1;
				num_1 += num_0;
				num_0 = temp_num;
			}
			sol.push_back(num_0);
			sol.push_back(num_1);
		}
	}
	for (int i = 0; i < sol.size(); i++)
	{
		cout << sol.at(i++) << " ";
		cout << sol.at(i) << endl;
	}
}