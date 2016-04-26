#include <iostream>

using std::cin;
using std::cout;
using std::endl;

#define MAXN 100009

int P[MAXN];
int q[MAXN];

void insert(int *q, int i, int v) {
	q[i] = v;
	int j = i / 2;
	int tmp = 0;
	while (i > 1 && q[i] > q[j]) {
		tmp = q[i];
		q[i] = q[j];
		q[j] = tmp;
		i = j;
		j = i / 2;
	}
}

int delete_max(int *q, int k) {
	int res = q[1];
	q[1] = q[k];
	int n = k - 1;
	int i = 1;
	int j = 2 * i;
	int tmp = 0;
	while (j <= n) {
		if (j + 1 <= n&&q[j + 1] > q[j]) {
			j += 1;
		}
		if (q[i] >= q[j]) {
			break;
		}
		tmp = q[i];
		q[i] = q[j];
		q[j] = tmp;
		i = j;
		j = 2 * i;
	}
	return res;
}

int main() {
	int N = 0;
	long long Q = 0;
	cin >> N >> Q;
	for (int i = 1; i <= N; i++) {
		cin >> P[i];
	}
	int min_k = N + 1;
	int low = 1;
	int high = N;
	while (low <= high) {
		for (int i = 0; i <= N + 1; i++) {
			q[i] = 0;
		}
		int k = (low + high) / 2;
		for (int i = 1; i <= k; i++) {
			insert(q, i, P[i]);
		}
		long long sp = 0;
		int n = 0;
		for (int j = k + 1; j <= N; j++) {
			if (sp > Q) {
				break;
			}
			int v = delete_max(q, k);
			n += 1;
			sp += v * n;
			insert(q, k, P[j]);
		}
		for (int j = 0; j < k; j++) {
			if (sp > Q) {
				break;
			}
			int v = delete_max(q, k - j);
			n += 1;
			sp += v * n;
		}
		if (sp <= Q) {
			if (min_k > k) {
				min_k = k;
			}
			high = k - 1;
		}
		else {
			low = k + 1;
		}
	}
	if (min_k <= N) {
		cout << min_k << endl;
	}
	else {
		cout << "-1" << endl;
	}
	return 0;
}