#include <iostream>
#include <vector>
#include <map>

using std::vector;
using std::map;
using std::cin;
using std::cout;
using std::endl;

int maze[110][110];
int min_change = 10000;
int N, M;
/*
Time Limit Exceed
*/
void next_step(int i, int j, int change, bool right) {
	if (change > min_change || i > N || j > M) {
		return;
	}
	//cout << i << " " << j << " " << change << endl;
	if (i == N && j == M) {
		if (change < min_change) {
			min_change = change;
		}
		return;
	}
	if (right) {
		if (j < M) {
			next_step(i, j + 1, change + maze[i][j + 1], true);
		}
		next_step(i + 1, j, change + maze[i + 1][j] + 1 - maze[i][j + 1], false);
	}
	else {
		if (i < N) {
			next_step(i + 1, j, change + maze[i + 1][j], false);
		}
		next_step(i, j + 1, change + maze[i][j + 1] + 1 - maze[i + 1][j], true);
	}
}

int min(int a, int b) {
	return a < b ? a : b;
}
//DP! DP! DP!
int res_right[110][110];
int res_down[110][110];
void next_step2() {
	res_right[1][1] = maze[1][1];
	res_down[1][1] = 1 - maze[1][2];
	for (int j = 2; j <= M; j++) {
		res_right[1][j] = res_right[1][j - 1] + maze[1][j];
		res_down[1][j] = res_right[1][j - 1] + 1 - maze[1][j + 1];
	}
	for (int i = 2; i <= N; i++) {
		res_down[i][1] = res_down[i - 1][1] + maze[i][1];
		res_right[i][1] = res_down[i - 1][1] + 1 - maze[i + 1][1];
	}
	for (int i = 2; i <= N; i++) {
		for (int j = 2; j <= M; j++) {
			res_right[i][j] = maze[i][j] + min(res_right[i][j - 1], res_down[i - 1][j] + 1 - maze[i + 1][j]);
			res_down[i][j] = maze[i][j] + min(res_down[i - 1][j], res_right[i][j - 1] + 1 - maze[i][j + 1]);
		}
	}
}

int main() {
	cin >> N >> M;
	char c;
	for (int i = 0; i < N + 2; i++) {
		for (int j = 0; j < M + 2; j++) {
			maze[i][j] = 1;
		}
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> c;
			if (c == '.') {
				maze[i][j] = 0;
			}
			else {
				maze[i][j] = 1;
			}
		}
	}
	//if (maze[1][1] == 1) {
	//	next_step(1, 1, 1, true);
	//}
	//else {
	//	next_step(1, 1, 0, true);
	//}
	//cout << min_change;
	next_step2();
	cout << min(res_right[N][M], res_down[N][M]);

	return 0;
}