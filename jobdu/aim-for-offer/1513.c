#include <stdio.h>

int main() {
	int i, n, sum;
	unsigned t;
	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++) {
			scanf("%u", &t);
			sum = 0;
			while(t) {
				sum += t % 2;
				t = t / 2;
			}
			printf("%d\n", sum);
		}
	}
}