#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::ceil;

int main() {
	int test;
	cin >> test;
	for (int i = 0; i < test; i++) {
		int N, P, W, H;
		int a[1009];
		cin >> N >> P >> W >> H;
		for (int j = 0; j < N; j++) {
			cin >> a[j];
		}
		int S = 0;
		while (true) {
			int col_chs = W / (S + 1);
			int rows = H / (S + 1);
			int total_rows = 0;
			for (int i = 0; i < N; i++) {
				total_rows += (int)ceil(a[i] * 1.0 / col_chs);
			}
			int pages = (int)ceil(total_rows * 1.0 / rows);
			if (pages < P) {
				S += 1;
			}
			else if (pages == P) {
				S += 1;
				break;
			}
			else {
				break;
			}
		}
		cout << S << endl;
	}
	return 0;
}