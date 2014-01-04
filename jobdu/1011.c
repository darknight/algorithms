#include <stdio.h>

int main() {

	int t, from, to, max;
	int num[10000], i, k;
	int m;

	while(scanf("%d", &k) && k) {
		for(i = 1; i <= k; i++)
			scanf("%d", &num[i]);
		from = to = 1;
		m = max = num[1];
		for(i = 2; i <= k; i++) {
			if(m < 0) {
				m = num[i];
				t = i;
			}
			else m += num[i];
			if(m > max) {
				max = m;
				from = t;
				to = i;
			}
		}
		printf("%d %d %d\n", max, num[from], num[to]);
	}
}
