#include <stdio.h>

#define MAX 0x7FFFFFFF

int main() {

	int n, q[256];
	int i, j, k;
	int min, max, sum;

	while(scanf("%d", &n) != EOF) {
		min = MAX;
		max = -1;
		for(i = 0; i < n; i++) {
			scanf("%d", q+i);
			if(q[i] < min) {
				min = q[i];
				j = i;
			}
			if(q[i] >= max) {
				max = q[i];
				k = i;
			}
		}
		sum = j + n - k -1;
		if(j > k) sum -= 1;
		printf("%d\n", sum);
	}
}
